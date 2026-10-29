# Goal

**Build a free AI market analyst for US and Indian stocks. Its probability
forecasts have to beat simple baselines on data it has never seen, and it has to
know which market regime it is in.**

## What "accuracy" means here

Each forecast is a probability: P(this stock or index closes higher 2 trading
days from now), made after every close. Later layers add a 4-week horizon.

- **Primary metric: Brier score**, the mean of (forecast − outcome)², lower is
  better. It rewards being right *and* being honest about confidence.
- **Hit rate is reported but is not the target.** Markets drift up, so always
  saying "up" already scores about 53% on our watchlist since 2010 (54% in the
  US). A 55% hit rate is not an edge.
- **Skill** = 1 − Brier(model) / Brier(base_rate). Positive means better than
  the baseline.

## Targets

| | Target | How it's checked |
|---|---|---|
| Must | Brier better than `base_rate`, p < 0.05 | `compare()` in `scorecard.py`: losses grouped by day, Newey-West for overlap |
| Must | Calibrated: each probability bucket within ±3 points of the observed frequency | `calibration()` |
| Must | No worse than `base_rate` inside the **stressed** regime | Scorecard split by regime (layer 2) |
| Stretch | Skill ≥ +0.5% at 2 days, ≥ +2% at 4 weeks | Same scorecard |

Only **forward** results count for the AI layers: forecasts logged before the
outcome is known. AI models already know how past markets played out, so their
backtests are contaminated. Backtests are fine for the math layers, which only
see data up to each forecast date.

## The bar to beat (layer 1, 2-day horizon, 2010 to Oct 2026)

| | Brier | Hit rate |
|---|---|---|
| `base_rate` (all) | 0.2493 | 52.6% |
| `momentum` (all) | 0.2493 | 52.3% |

12-week momentum does **not** beat the base rate (on weekly forecasts it was
significantly worse in India, p = 0.015). The stretch target is that small
(+0.5%) because short-horizon stock direction is close to a coin flip. Anything
claiming much more is probably leaking the future.

## Rules

- **Budget ₹0:** free data and free model tiers only.
- **Kill rule:** any component that doesn't beat `base_rate` after 52 forward
  weeks gets removed.
- **Statistical honesty:** a year of forward results (~250 days) can only
  confirm a large edge. A small edge needs years. We say which one we have.
- **Out of scope:** executing trades, intraday prediction, financial advice.

## Milestones

1. ✅ **Layer 1**: baselines, regime model, scorecard (`layer1.py`)
2. ✅ **Loop**: GitHub Actions after every trading day, append-only forecast log on the `results` branch
3. ✅ **Layer 2**: gradient-boosting model with walk-forward validation, a walk-forward regime model, and the scorecard split by regime
4. ✅ **Layer 3 (v1)**: one Gemini call per ticker per day on price facts plus the last 3 days of Google News headlines (`layer3.py`), scored forward only. The full TradingAgents pipeline costs dozens of calls per stock and waits until this cheap version shows any signal.
5. **Reviews** at 26 and 52 forward weeks against this file

## Experiment log

Every variant tried is listed here, because trying many and keeping the best is
how backtests lie. A result is judged against how many attempts it took.

| # | Date | Experiment | Backtest result (2-day, 2010 on) | Decision |
|---|---|---|---|---|
| 1 | 2026-10-29 | 12-week momentum, weekly horizon | Worse than base rate, India p = 0.015 | Superseded by #2 |
| 2 | 2026-10-29 | 60-day momentum, 2-day horizon | Brier 0.2493, same as base rate, p = 0.18 | Kept as baseline |
| 3 | 2026-10-29 | GBM on 12 price/regime features, annual walk-forward, no tuning | Brier 0.2497, **worse** than base rate (p = 0.022), overconfident | Kept in the forward log for the kill rule; not tuned |
| 4 | 2026-10-29 | AI analyst v1: Gemini 3.5 Flash Lite, price facts + headlines published before the next session opens, prompt fixed in advance | Forward only, no backtest possible | Logging from 2026-10-29 |

**Lesson from #3:** price-only features at a 2-day horizon carry no usable edge
for these large caps. An edge has to come from information that isn't in the
price history (news, fundamentals, flows, events) or from horizons where
documented effects exist.
