"""Layer 1: baselines, market regimes and the scorecard, on free Yahoo data.

Every forecast is P(this ticker closes higher HORIZON trading days from now),
made from data up to today's close only. Anything later (models, AI agents)
has to beat these numbers.

    python layer1.py      # appends to forecasts/log.csv, writes reports/layer1.md

RESULTS_DIR (default ".") is where the log and report live; in the loop it is
a checkout of the results branch.
"""
import os
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf
from hmmlearn.hmm import GaussianHMM

from layer2 import features, stress_prob, walk_forward
from scorecard import calibration, compare, score

# ponytail: today's large caps, so the history carries survivorship bias; fine for
# baselines, use point-in-time index members before trusting stock-level results.
MARKETS = {
    "US": ["^GSPC", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "JPM", "XOM", "JNJ", "PG", "WMT"],
    "India": ["^NSEI", "RELIANCE.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "TCS.NS",
              "BHARTIARTL.NS", "ITC.NS", "LT.NS", "SBIN.NS", "HINDUNILVR.NS"],
}
INDEX = {"US": "^GSPC", "India": "^NSEI"}
HORIZON = 2          # trading days
MOMENTUM_DAYS = 60   # ~12 weeks
SCORE_FROM = "2010-01-01"
MODELS = ["base_rate", "momentum", "gbm"]
RESULTS = Path(os.environ.get("RESULTS_DIR", "."))
LOG = RESULTS / "forecasts" / "log.csv"


def daily_closes(tickers):
    d = yf.download(tickers, start="2000-01-01", progress=False, auto_adjust=True)["Close"]
    now = datetime.now(timezone.utc)
    if (now.hour, now.minute) < (21, 30):  # today's bar is unfinished until both markets close
        d = d[d.index.date < now.date()]
    return d


def conditional_rate(state, up_next, h=HORIZON):
    """P(up over the next h days | today's state), from outcomes already known.

    The outcome of day k is known at k+h, so the forecast at t uses k <= t-h only.
    Beta(1,1) prior, so a state seen few times stays near 50%.
    """
    p = pd.Series(np.nan, index=state.index)
    for s in state.dropna().unique():
        m = state == s
        hits = up_next.where(m).fillna(0).cumsum().shift(h, fill_value=0)
        n = (m & up_next.notna()).cumsum().shift(h, fill_value=0)
        p[m] = ((1 + hits) / (2 + n))[m]
    return p


def outcome(close, h=HORIZON):
    nxt = close.shift(-h) / close - 1
    return (nxt > 0).astype(float).where(nxt.notna())


def forecasts(close):
    up_next = outcome(close)
    return pd.DataFrame({
        "y": up_next,
        "base_rate": conditional_rate(pd.Series(0, index=close.index), up_next),
        "momentum": conditional_rate(np.sign(close.pct_change(MOMENTUM_DAYS)), up_next),
    })


def regimes(close, n=2):
    """2-state Gaussian HMM on weekly log returns, states ordered by volatility.

    Three states flip almost every week on returns alone, so two it is.
    ponytail: fit on the full history, so it describes regimes and must not be
    scored as a forecast; walk-forward refits before it feeds a model.
    """
    r = np.log(close.resample("W-FRI").last()).diff().dropna()
    x = r.to_numpy().reshape(-1, 1)
    hmm = GaussianHMM(n, covariance_type="full", n_iter=500, random_state=0).fit(x)
    order = np.argsort(hmm.covars_.reshape(n))
    post = hmm.predict_proba(x)[:, order]
    mu, sd = hmm.means_.ravel()[order], np.sqrt(hmm.covars_.reshape(n))[order]
    stay = np.diag(hmm.transmat_)[order]
    return pd.DataFrame({
        "ann_return": mu * 52, "ann_vol": sd * np.sqrt(52),
        "time_share": post.mean(0), "avg_weeks": 1 / (1 - stay), "now": post[-1],
    }, index=["calm", "stressed"][:n])


def append_log(live):
    """Append today's forecasts; never rewrite what is already logged."""
    rows = live.melt(["date", "ticker", "market"], MODELS, "model", "p")
    rows.insert(0, "made_at", datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ"))
    rows["date"] = rows["date"].dt.strftime("%Y-%m-%d")
    rows["horizon"] = HORIZON
    if LOG.exists():
        seen = pd.read_csv(LOG, usecols=["date", "ticker", "model"]).astype(str)
        keys = set(map(tuple, seen.to_numpy()))
        rows = rows[[k not in keys for k in map(tuple, rows[["date", "ticker", "model"]].to_numpy())]]
    LOG.parent.mkdir(parents=True, exist_ok=True)
    rows.round({"p": 4}).to_csv(LOG, mode="a", header=not LOG.exists(), index=False)
    return len(rows)


def forward_scores(closes):
    """Score logged forecasts whose outcome is now known."""
    if not LOG.exists():
        return None
    log = pd.read_csv(LOG, parse_dates=["date"])
    ys = {t: outcome(closes[t].dropna()) for t in log["ticker"].unique() if t in closes}
    log["y"] = [ys[t].get(d, np.nan) if t in ys else np.nan for t, d in zip(log["ticker"], log["date"])]
    return log.dropna(subset=["y"]).pivot_table(index=["date", "ticker", "market", "y"],
                                                columns="model", values="p").reset_index()


def scorecard_section(df, title, by=("market",)):
    out = []
    groups = [("All", df)] + [(name, g) for col in by for name, g in df.groupby(col)]
    for name, g in groups:
        g = g.dropna(subset=MODELS)  # forecasts logged before a model existed are skipped
        s = pd.DataFrame({m: score(g.assign(p=g[m])) for m in MODELS}).T
        out += [f"## {title}: {name}", "", "```", s.round(4).to_string(), "```"]
        for m in MODELS[1:]:
            gain, pval = compare(g, m, "base_rate", lags=HORIZON - 1)
            out.append(f"{m} vs base_rate: Brier gain per day {gain:+.5f}, p = {pval:.3f}  ")
        out.append("")
    return out


def main():
    rows, closes, out = [], {}, ["# Layer 1 report", "", f"Horizon: {HORIZON} trading days.", ""]
    for market, tickers in MARKETS.items():
        c = daily_closes(tickers)
        idx = c[INDEX[market]].dropna()
        stress = stress_prob(idx)
        for t in tickers:
            s = c[t].dropna()
            if s.empty:
                raise SystemExit(f"no data for {t}")  # fail loudly, the loop emails on failure
            closes[t] = s
            f = forecasts(s).join(features(s, idx, stress, market == "India")).assign(ticker=t, market=market)
            rows.append(f.rename_axis("date").reset_index())
        out += [f"## {market} regime (as of {closes[INDEX[market]].index[-1]:%Y-%m-%d})", "", "```",
                regimes(closes[INDEX[market]]).round(3).to_string(), "```", ""]

    df = pd.concat(rows, ignore_index=True)
    df["gbm"] = walk_forward(df, int(SCORE_FROM[:4]))
    df["regime"] = np.where(df["stress"] > 0.5, "stressed", "calm")
    live = df.groupby("ticker").tail(1).dropna(subset=MODELS)
    added = append_log(live)
    back = df[df["date"] >= SCORE_FROM].dropna(subset=["y", *MODELS])

    fwd = forward_scores(closes)
    if fwd is None or fwd["date"].nunique() < 20:
        n = 0 if fwd is None else fwd["date"].nunique()
        out += ["## Forward scorecard", "", f"{n} scored forecast dates so far; shown from 20.", ""]
    else:
        out += scorecard_section(fwd, "Forward scorecard (logged before outcome)")

    out += scorecard_section(back, f"Backtest ({SCORE_FROM[:4]} on, walk-forward)", by=("market", "regime"))
    out += ["## GBM calibration (backtest, all)", "", "```",
            calibration(back.assign(p=back["gbm"])).round(3).to_string(), "```", "",
            f"## Latest forecasts: P(up over next {HORIZON} trading days), {added} new rows logged", "", "```",
            live.assign(date=live["date"].dt.date).set_index(["market", "ticker"])[["date", *MODELS]]
                .round(3).to_string(), "```"]

    (RESULTS / "reports").mkdir(parents=True, exist_ok=True)
    (RESULTS / "reports" / "layer1.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
