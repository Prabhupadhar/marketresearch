"""Scoring for probability forecasts. A forecast is P(up over the horizon); y is 1 if it went up."""
import numpy as np
import pandas as pd
from scipy.stats import norm


def brier(p, y):
    return (np.asarray(p, float) - np.asarray(y, float)) ** 2


def score(df):
    """df has columns p, y. Brier skill is measured against the in-sample up-frequency."""
    p, y = df["p"].to_numpy(float), df["y"].to_numpy(float)
    b = brier(p, y).mean()
    ref = brier(np.full_like(y, y.mean()), y).mean()
    return {"n": len(y), "hit_rate": ((p >= 0.5) == y).mean(), "brier": b, "brier_skill": 1 - b / ref}


def compare(df, a, b, lags=0):
    """Diebold-Mariano test: is model a's Brier loss lower than model b's?

    Losses are averaged per date first, because tickers on the same day move
    together and are not independent samples. Forecasts over h days overlap,
    so the variance uses Newey-West with lags = h - 1.
    Returns (mean daily gain, two-sided p).
    """
    d = pd.Series(brier(df[b], df["y"]) - brier(df[a], df["y"])).groupby(df["date"].to_numpy()).mean().to_numpy()
    n, e = len(d), d - d.mean()
    var = e @ e / n + 2 * sum((1 - k / (lags + 1)) * (e[k:] @ e[:-k]) / n for k in range(1, lags + 1))
    return d.mean(), 2 * norm.sf(abs(d.mean() / np.sqrt(var / n)))


def calibration(df, bins=(0, 0.45, 0.5, 0.55, 0.6, 1)):
    """Forecast vs observed up-frequency per probability bucket."""
    g = df.groupby(pd.cut(df["p"], bins), observed=True)
    return pd.DataFrame({"n": g.size(), "forecast": g["p"].mean(), "observed": g["y"].mean()})
