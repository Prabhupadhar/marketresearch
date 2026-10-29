# Goal

**Build a free AI market analyst for US and Indian stocks. Its probability
forecasts have to beat simple baselines on data it has never seen, and it has to
know which market regime it is in.**

## What "accuracy" means here

Each forecast is a probability: P(this stock or index is up next week). Later
layers add a 4-week horizon.

- **Primary metric: Brier score**, the mean of (forecast − outcome)², lower is
  better. It rewards being right *and* being honest about confidence.
- **Hit rate is reported but is not the target.** Markets drift up, so always
  saying "up" already scores 54% on our watchlist since 2010. A 55% hit rate is
  not an edge.
- **Skill** = 1 − Brier(model) / Brier(base_rate). Positive means better than
  the baseline.

## Targets

| | Target | How it's checked |
|---|---|---|
| Must | Brier better than `base_rate`, p < 0.05 | `compare()` in `scorecard.py`, losses grouped by week |
| Must | Calibrated: each probability bucket within ±3 points of the observed frequency | `calibration()` |
| Must | No worse than `base_rate` inside the **stressed** regime | Scorecard split by regime (layer 2) |
| Stretch | Skill ≥ +0.5% weekly, ≥ +2% at 4 weeks | Same scorecard |

Only **forward** results count for the AI layers: forecasts logged before the
outcome is known. AI models already know how past markets played out, so their
backtests are contaminated. Backtests are fine for the math layers, which only
see data up to each forecast date.

## The bar to beat (layer 1, weekly, 2010 to Oct 2026)

| | Brier | Hit rate |
|---|---|---|
| `base_rate` (all) | 0.2485 | 54.2% |
| `momentum` (all) | 0.2488 | 53.9% |

12-week momentum does **not** beat the base rate. It is significantly worse in
India (p = 0.015). The stretch target is that small (+0.5%) because weekly stock
direction is close to a coin flip. Anything claiming much more is probably
leaking the future.

## Rules

- **Budget ₹0:** free data and free model tiers only.
- **Kill rule:** any component that doesn't beat `base_rate` after 52 forward
  weeks gets removed.
- **Statistical honesty:** 52 weeks of forward results can only confirm a large
  edge. A small edge needs years. We say which one we have.
- **Out of scope:** executing trades, intraday prediction, financial advice.

## Milestones

1. ✅ **Layer 1**: baselines, regime model, scorecard (`layer1.py`)
2. **Layer 2**: gradient-boosting model with walk-forward validation, a walk-forward regime model, and the scorecard split by regime
3. **Layer 3**: AI agents (TradingAgents on free models plus a market-conditions agent) writing to a dated forecast log
4. **Layer 4**: a weekly GitHub Actions loop that scores itself
5. **Reviews** at 26 and 52 forward weeks against this file
