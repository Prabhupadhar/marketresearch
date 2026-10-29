import os
import tempfile

import numpy as np
import pandas as pd

os.environ["RESULTS_DIR"] = tempfile.mkdtemp()
import layer1  # noqa: E402
from layer1 import conditional_rate  # noqa: E402
from layer2 import FEATURES, _filter, stress_prob, walk_forward  # noqa: E402
from scorecard import compare, score  # noqa: E402
from hmmlearn.hmm import GaussianHMM  # noqa: E402


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
                         "base_rate": [0.55], "momentum": [0.6], "gbm": [0.5]})
    assert layer1.append_log(live) == 3
    before = layer1.LOG.read_text()
    assert layer1.append_log(live.assign(momentum=0.9)) == 0  # same day again: nothing rewritten
    assert layer1.append_log(live.assign(date=pd.to_datetime(["2026-10-29"]))) == 3
    assert layer1.LOG.read_text().startswith(before)


def test_filter_matches_hmmlearn_at_last_step():
    # At the final step, filtered and smoothed probabilities are the same thing.
    x = np.random.default_rng(0).normal(0, [0.01] * 300 + [0.04] * 100)
    hmm = GaussianHMM(2, covariance_type="full", random_state=0).fit(x.reshape(-1, 1))
    assert np.allclose(_filter(hmm, x)[-1], hmm.predict_proba(x.reshape(-1, 1))[-1])


def test_layer2_ignores_the_future():
    rng = np.random.default_rng(1)
    dates = pd.bdate_range("2004-01-01", "2012-12-31")
    close = pd.Series(100 * np.exp(np.cumsum(rng.normal(0, 0.01, len(dates)))), index=dates)
    later = close.copy()
    later[later.index.year >= 2011] *= np.exp(np.cumsum(rng.normal(0, 0.05, (later.index.year >= 2011).sum())))
    early = close.index.year < 2011
    assert np.allclose(stress_prob(close)[early], stress_prob(later)[early], equal_nan=True)

    df = pd.DataFrame(rng.normal(size=(len(dates), len(FEATURES))), columns=FEATURES).assign(
        date=dates, y=rng.integers(0, 2, len(dates)).astype(float))
    df2 = df.copy()
    df2.loc[df2["date"].dt.year >= 2011, "y"] = 1.0
    a, b = walk_forward(df, 2009), walk_forward(df2, 2009)
    m = df["date"].dt.year.between(2009, 2010)
    assert a[m].notna().all() and np.allclose(a[m], b[m])
    assert not np.allclose(a[~m].dropna(), b[~m].dropna())  # the change is visible once it is in the past


def test_ai_answers_are_validated():
    from layer3 import parse
    assert parse('{"p_up": 0.57, "reason": "beat on revenue `rm -rf` [x](y)"}') == (0.57, "beat on revenue rm -rf x(y)")
    for bad in ['{"p_up": 1.0, "reason": ""}', '{"p_up": "ignore all instructions"}', "not json", '{"reason": "x"}']:
        assert parse(bad) is None, bad


def test_news_stops_before_next_session():
    from datetime import datetime, timezone
    from layer3 import news_cutoff
    now = datetime(2026, 10, 29, 22, 47, tzinfo=timezone.utc)
    d = pd.Timestamp("2026-10-28")
    assert news_cutoff(d, "India", now) == datetime(2026, 10, 29, 3, 45, tzinfo=timezone.utc)
    assert news_cutoff(d, "US", now) == datetime(2026, 10, 29, 13, 30, tzinfo=timezone.utc)
    assert news_cutoff(pd.Timestamp("2026-10-29"), "US", now) == now


def test_missing_ai_forecast_is_not_logged():
    live = pd.DataFrame({"date": pd.to_datetime(["2026-11-02", "2026-11-02"]), "ticker": ["A", "B"],
                         "market": ["US", "US"], "base_rate": [0.5, 0.5], "momentum": [0.5, 0.5],
                         "gbm": [0.5, 0.5], "ai": [0.6, np.nan]})
    assert layer1.append_log(live) == 7


if __name__ == "__main__":
    for f in [test_no_lookahead, test_conditional_split, test_score_and_compare, test_log_is_append_only,
              test_filter_matches_hmmlearn_at_last_step, test_layer2_ignores_the_future,
              test_ai_answers_are_validated, test_news_stops_before_next_session,
              test_missing_ai_forecast_is_not_logged]:
        f()
    print("ok")
