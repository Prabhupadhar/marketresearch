# Layer 1 report

Horizon: 2 trading days.

## US regime (as of 2026-10-28)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.156    0.115       0.752     42.492  0.977
stressed      -0.221    0.296       0.248     13.509  0.023
```

## India regime (as of 2026-10-28)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.115    0.140       0.843    184.045  0.994
stressed      -0.103    0.371       0.157     28.193  0.006
```

## Forward scorecard

0 scored forecast dates so far; shown from 20.

## Backtest (2010 on): All

```
                 n  hit_rate   brier  brier_skill
base_rate  92148.0    0.5264  0.2493      -0.0009
momentum   92148.0    0.5234  0.2493      -0.0012
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.180

## Backtest (2010 on): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45629.0    0.5123  0.2500      -0.0011
momentum   45629.0    0.5105  0.2501      -0.0016
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.189

## Backtest (2010 on): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46519.0    0.5403  0.2486      -0.0022
momentum   46519.0    0.5360  0.2486      -0.0023
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.841

## Momentum calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]     56     0.442     0.589
(0.45, 0.5]  11419     0.493     0.530
(0.5, 0.55]  75961     0.524     0.530
(0.55, 0.6]   4709     0.558     0.556
(0.6, 1.0]       3     0.667     0.333
```

## Latest forecasts: P(up over next 2 trading days), 44 new rows logged

```
                            date  base_rate  momentum
market ticker                                        
US     ^GSPC          2026-10-28      0.556     0.570
       AAPL           2026-10-28      0.541     0.551
       MSFT           2026-10-28      0.524     0.532
       NVDA           2026-10-28      0.533     0.543
       AMZN           2026-10-28      0.520     0.525
       GOOGL          2026-10-28      0.544     0.532
       JPM            2026-10-28      0.528     0.519
       XOM            2026-10-28      0.526     0.526
       JNJ            2026-10-28      0.528     0.533
       PG             2026-10-28      0.525     0.515
       WMT            2026-10-28      0.523     0.516
India  ^NSEI          2026-10-28      0.537     0.528
       RELIANCE.NS    2026-10-28      0.518     0.525
       HDFCBANK.NS    2026-10-28      0.518     0.532
       ICICIBANK.NS   2026-10-28      0.514     0.527
       INFY.NS        2026-10-28      0.520     0.517
       TCS.NS         2026-10-28      0.494     0.521
       BHARTIARTL.NS  2026-10-28      0.513     0.517
       ITC.NS         2026-10-28      0.515     0.517
       LT.NS          2026-10-28      0.521     0.508
       SBIN.NS        2026-10-28      0.520     0.511
       HINDUNILVR.NS  2026-10-28      0.510     0.527
```
