# Layer 1 report

## US regime (week of 2026-10-23)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.155    0.115       0.752     42.468  0.974
stressed      -0.222    0.297       0.248     13.490  0.026
```

## India regime (week of 2026-10-23)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.115    0.140       0.843    183.875  0.988
stressed      -0.103    0.372       0.157     28.203  0.012
```

## Scorecard: All (weekly, 2010 on)

```
                 n  hit_rate   brier  brier_skill
base_rate  19294.0    0.5419  0.2485      -0.0022
momentum   19294.0    0.5386  0.2488      -0.0036
```
momentum vs base_rate: weekly Brier gain -0.00035, p = 0.037

## Scorecard: India (weekly, 2010 on)

```
                n  hit_rate   brier  brier_skill
base_rate  9647.0    0.5311  0.2494      -0.0021
momentum   9647.0    0.5286  0.2500      -0.0043
```
momentum vs base_rate: weekly Brier gain -0.00055, p = 0.015

## Scorecard: US (weekly, 2010 on)

```
                n  hit_rate   brier  brier_skill
base_rate  9647.0    0.5527  0.2475      -0.0035
momentum   9647.0    0.5486  0.2476      -0.0041
```
momentum vs base_rate: weekly Brier gain -0.00014, p = 0.538

## Momentum calibration (all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]      2     0.447     1.000
(0.45, 0.5]   1349     0.491     0.551
(0.5, 0.55]  10842     0.528     0.545
(0.55, 0.6]   6621     0.566     0.546
(0.6, 1.0]     480     0.607     0.542
```

## Latest forecasts: P(up next week)

```
                            date  base_rate  momentum
market ticker                                        
US     ^GSPC          2026-10-23      0.561     0.576
       AAPL           2026-10-23      0.574     0.600
       MSFT           2026-10-23      0.531     0.540
       NVDA           2026-10-23      0.537     0.551
       AMZN           2026-10-23      0.530     0.518
       GOOGL          2026-10-23      0.560     0.534
       JPM            2026-10-23      0.540     0.536
       XOM            2026-10-23      0.539     0.533
       JNJ            2026-10-23      0.549     0.556
       PG             2026-10-23      0.554     0.554
       WMT            2026-10-23      0.541     0.522
India  ^NSEI          2026-10-23      0.559     0.553
       RELIANCE.NS    2026-10-23      0.553     0.561
       HDFCBANK.NS    2026-10-23      0.541     0.560
       ICICIBANK.NS   2026-10-23      0.534     0.527
       INFY.NS        2026-10-23      0.554     0.567
       TCS.NS         2026-10-23      0.520     0.548
       BHARTIARTL.NS  2026-10-23      0.526     0.520
       ITC.NS         2026-10-23      0.521     0.537
       LT.NS          2026-10-23      0.550     0.532
       SBIN.NS        2026-10-23      0.531     0.524
       HINDUNILVR.NS  2026-10-23      0.513     0.534
```
