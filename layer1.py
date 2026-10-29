"""Layer 1: baselines, market regimes and the scorecard, on free Yahoo data.

Every forecast is P(this ticker is up next week), made from data up to this
week only. Anything later (models, AI agents) has to beat these numbers.

    python layer1.py      # writes reports/layer1.md
"""
from pathlib import Path

import numpy as np
import pandas as pd
import yfinance as yf
from hmmlearn.hmm import GaussianHMM

from scorecard import calibration, compare, score

# ponytail: today's large caps, so the history carries survivorship bias; fine for
# baselines, use point-in-time index members before trusting stock-level results.
MARKETS = {
    "US": ["^GSPC", "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "JPM", "XOM", "JNJ", "PG", "WMT"],
    "India": ["^NSEI", "RELIANCE.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "TCS.NS",
              "BHARTIARTL.NS", "ITC.NS", "LT.NS", "SBIN.NS", "HINDUNILVR.NS"],
}
INDEX = {"US": "^GSPC", "India": "^NSEI"}
SCORE_FROM = "2010-01-01"
MODELS = ["base_rate", "momentum"]


def weekly_closes(tickers):
    d = yf.download(tickers, start="2000-01-01", progress=False, auto_adjust=True)["Close"]
    w = d.resample("W-FRI").last()
    return w[w.index <= d.index[-1]]  # drop the week still in progress


def conditional_rate(state, up_next):
    """P(up next week | this week's state), from outcomes already known.

    The outcome of week k is known at k+1, so the forecast at t uses k < t only.
    Beta(1,1) prior, so a state seen few times stays near 50%.
    """
    p = pd.Series(np.nan, index=state.index)
    for s in state.dropna().unique():
        m = state == s
        hits = up_next.where(m).fillna(0).cumsum().shift(1, fill_value=0)
        n = (m & up_next.notna()).cumsum().shift(1, fill_value=0)
        p[m] = ((1 + hits) / (2 + n))[m]
    return p


def forecasts(close):
    nxt = close.pct_change().shift(-1)
    up_next = (nxt > 0).astype(float).where(nxt.notna())
    return pd.DataFrame({
        "y": up_next,
        "base_rate": conditional_rate(pd.Series(0, index=close.index), up_next),
        "momentum": conditional_rate(np.sign(close.pct_change(12)), up_next),
    })


def regimes(close, n=2):
    """2-state Gaussian HMM on weekly log returns, states ordered by volatility.

    ponytail: fit on the full history, so it describes regimes and must not be
    scored as a forecast; walk-forward refits before it feeds a model.
    """
    r = np.log(close).diff().dropna()
    x = r.to_numpy().reshape(-1, 1)
    hmm = GaussianHMM(n, covariance_type="full", n_iter=500, random_state=0).fit(x)
    order = np.argsort(hmm.covars_.reshape(n))
    post = hmm.predict_proba(x)[:, order]
    mu, sd = hmm.means_.ravel()[order], np.sqrt(hmm.covars_.reshape(n))[order]
    stay = np.diag(hmm.transmat_)[order]
    return pd.DataFrame({
        "ann_return": mu * 52, "ann_vol": sd * np.sqrt(52),
        "time_share": post.mean(0), "avg_weeks": 1 / (1 - stay), "now": post[-1],
    }, index=["calm", "stressed"][:n]), r.index[-1]


def main():
    rows, out = [], ["# Layer 1 report", ""]
    for market, tickers in MARKETS.items():
        closes = weekly_closes(tickers)
        for t in tickers:
            f = forecasts(closes[t].dropna()).assign(ticker=t, market=market)
            rows.append(f.rename_axis("date").reset_index())

        table, asof = regimes(closes[INDEX[market]].dropna())
        out += [f"## {market} regime (week of {asof:%Y-%m-%d})", "", "```",
                table.round(3).to_string(), "```", ""]

    df = pd.concat(rows)
    live = df[df["y"].isna()].dropna(subset=MODELS).assign(date=lambda x: x["date"].dt.date)  # latest week: outcome not known yet
    df = df[df["date"] >= SCORE_FROM].dropna(subset=["y", *MODELS])

    for market, g in [("All", df), *df.groupby("market")]:
        s = pd.DataFrame({m: score(g.assign(p=g[m])) for m in MODELS}).T
        gain, pval = compare(g, "momentum", "base_rate")
        out += [f"## Scorecard: {market} (weekly, {SCORE_FROM[:4]} on)", "", "```",
                s.round(4).to_string(), "```",
                f"momentum vs base_rate: weekly Brier gain {gain:+.5f}, p = {pval:.3f}", ""]

    out += ["## Momentum calibration (all)", "", "```",
            calibration(df.assign(p=df["momentum"])).round(3).to_string(), "```", "",
            "## Latest forecasts: P(up next week)", "", "```",
            live.set_index(["market", "ticker"])[["date", *MODELS]].round(3).to_string(), "```"]

    Path("reports").mkdir(exist_ok=True)
    Path("reports/layer1.md").write_text("\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    main()
