import numpy as np
import pandas as pd

from layer1 import conditional_rate
from scorecard import compare, score


def test_no_lookahead():
    # Outcome of week k becomes known at k+1, so forecast t may only use k < t.
    state = pd.Series([0, 0, 0, 0])
    up_next = pd.Series([1.0, 1.0, 0.0, np.nan])
    p = conditional_rate(state, up_next).tolist()
    assert p == [1 / 2, 2 / 3, 3 / 4, 3 / 5], p


def test_conditional_split():
    state = pd.Series([1, -1, 1, -1, 1])
    up_next = pd.Series([1.0, 0.0, 1.0, 0.0, np.nan])
    p = conditional_rate(state, up_next).tolist()
    assert p == [1 / 2, 1 / 2, 2 / 3, 1 / 3, 3 / 4], p


def test_score_and_compare():
    y = np.array([1, 0] * 50, float)
    df = pd.DataFrame({"date": np.arange(100), "y": y, "good": y * 0.8 + 0.1, "flat": 0.5})
    s = score(df.assign(p=df["good"]))
    assert s["hit_rate"] == 1 and abs(s["brier"] - 0.01) < 1e-12
    assert score(df.assign(p=df["flat"]))["brier_skill"] == 0
    gain, pval = compare(df.assign(flat=0.5 + 0.1 * np.sin(np.arange(100))), "good", "flat")
    assert gain > 0 and pval < 0.01


if __name__ == "__main__":
    for f in [test_no_lookahead, test_conditional_split, test_score_and_compare]:
        f()
    print("ok")
