import os
import tempfile

import numpy as np
import pandas as pd

os.environ["RESULTS_DIR"] = tempfile.mkdtemp()
import layer1  # noqa: E402
from layer1 import conditional_rate  # noqa: E402
from scorecard import compare, score  # noqa: E402


def test_no_lookahead():
    # Outcome of day k is known at k+h, so forecast t may only use k <= t-h.
    state = pd.Series([0] * 5)
    up_next = pd.Series([1.0, 1.0, 0.0, np.nan, np.nan])
    assert conditional_rate(state, up_next, h=1).tolist() == [1 / 2, 2 / 3, 3 / 4, 3 / 5, 3 / 5]
    assert conditional_rate(state, up_next, h=2).tolist() == [1 / 2, 1 / 2, 2 / 3, 3 / 4, 3 / 5]


def test_conditional_split():
    state = pd.Series([1, -1, 1, -1, 1])
    up_next = pd.Series([1.0, 0.0, 1.0, 0.0, np.nan])
    assert conditional_rate(state, up_next, h=1).tolist() == [1 / 2, 1 / 2, 2 / 3, 1 / 3, 3 / 4]


def test_score_and_compare():
    y = np.array([1, 0] * 50, float)
    df = pd.DataFrame({"date": np.arange(100), "y": y, "good": y * 0.8 + 0.1, "flat": 0.5})
    s = score(df.assign(p=df["good"]))
    assert s["hit_rate"] == 1 and abs(s["brier"] - 0.01) < 1e-12
    assert score(df.assign(p=df["flat"]))["brier_skill"] == 0
    for lags in (0, 1):
        gain, pval = compare(df.assign(flat=0.5 + 0.1 * np.sin(np.arange(100))), "good", "flat", lags)
        assert gain > 0 and pval < 0.01


def test_log_is_append_only():
    live = pd.DataFrame({"date": pd.to_datetime(["2026-10-28"]), "ticker": ["X"], "market": ["US"],
                         "base_rate": [0.55], "momentum": [0.6]})
    assert layer1.append_log(live) == 2
    before = layer1.LOG.read_text()
    assert layer1.append_log(live.assign(momentum=0.9)) == 0  # same day again: nothing rewritten
    assert layer1.append_log(live.assign(date=pd.to_datetime(["2026-10-29"]))) == 2
    assert layer1.LOG.read_text().startswith(before)


if __name__ == "__main__":
    for f in [test_no_lookahead, test_conditional_split, test_score_and_compare, test_log_is_append_only]:
        f()
    print("ok")
