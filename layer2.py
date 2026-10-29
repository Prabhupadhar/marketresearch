"""Layer 2: gradient boosting on price features, trained walk-forward.

Each year's forecasts come from a model trained only on earlier years, so the
backtest is out of sample. Also builds the walk-forward regime feature: the
filtered (past-only) probability that the market index is in its stressed state.
"""
import numpy as np
import pandas as pd
from hmmlearn.hmm import GaussianHMM
from scipy.stats import norm
from sklearn.ensemble import HistGradientBoostingClassifier

FEATURES = ["r1", "r5", "r20", "r60", "vol20", "vol_ratio", "ma200", "rel20",
            "idx_r5", "idx_vol20", "stress", "india"]


def _filter(hmm, x):
    """Forward-only state probabilities: P(state_t | returns up to t)."""
    like = norm.pdf(x[:, None], hmm.means_.ravel(), np.sqrt(hmm.covars_.reshape(-1)))
    a = hmm.startprob_ * like[0]
    out = [a / a.sum()]
    for row in like[1:]:
        a = (out[-1] @ hmm.transmat_) * row
        out.append(a / a.sum())
    return np.array(out)


def stress_prob(close):
    """P(stressed regime) per day, from an HMM refit each January on earlier data only."""
    r = np.log(close).diff().dropna()
    out = pd.Series(np.nan, index=r.index)
    for year in range(r.index[0].year + 3, r.index[-1].year + 1):
        past = r[r.index.year < year].to_numpy().reshape(-1, 1)
        hmm = GaussianHMM(2, covariance_type="full", n_iter=200, random_state=0).fit(past)
        upto = r[r.index.year <= year]
        probs = _filter(hmm, upto.to_numpy())[:, np.argmax(hmm.covars_.reshape(2))]
        this = upto.index.year == year
        out[upto.index[this]] = probs[this]
    return out.reindex(close.index)


def features(close, index, stress, india):
    lr = np.log(close).diff()
    vol20 = lr.rolling(20).std() * np.sqrt(252)
    idx = index.reindex(close.index).ffill()
    return pd.DataFrame({
        "r1": close.pct_change(), "r5": close.pct_change(5), "r20": close.pct_change(20),
        "r60": close.pct_change(60), "vol20": vol20,
        "vol_ratio": vol20 / (lr.rolling(60).std() * np.sqrt(252)),
        "ma200": close / close.rolling(200).mean() - 1,
        "rel20": close.pct_change(20) - idx.pct_change(20),
        "idx_r5": idx.pct_change(5),
        "idx_vol20": np.log(idx).diff().rolling(20).std() * np.sqrt(252),
        "stress": stress.reindex(close.index).ffill(), "india": float(india),
    })


def walk_forward(df, first_year):
    """df has date, y and FEATURES; returns P(up) for every row from first_year on.

    Rows within 7 days before each cutoff are purged from training: their
    outcomes are only known after the cutoff.
    ponytail: one refit per year and fixed hyperparameters (no tuning, so no
    multiple-testing penalty to pay); refit monthly if the edge looks real.
    """
    p = pd.Series(np.nan, index=df.index)
    for year in range(first_year, df["date"].dt.year.max() + 1):
        cut = pd.Timestamp(f"{year}-01-01")
        train = (df["date"] < cut - pd.Timedelta(days=7)) & df["y"].notna()
        test = df["date"].dt.year == year
        model = HistGradientBoostingClassifier(max_depth=3, learning_rate=0.05, max_iter=100,
                                               min_samples_leaf=500, l2_regularization=1.0,
                                               early_stopping=False, random_state=0)
        model.fit(df.loc[train, FEATURES], df.loc[train, "y"])
        p[test] = model.predict_proba(df.loc[test, FEATURES])[:, 1]
    return p
