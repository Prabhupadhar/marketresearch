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

## Backtest (2010 on, walk-forward): All

```
                 n  hit_rate   brier  brier_skill
base_rate  92148.0    0.5264  0.2493      -0.0009
momentum   92148.0    0.5235  0.2493      -0.0012
gbm        92148.0    0.5270  0.2497      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.182  
gbm vs base_rate: Brier gain per day -0.00047, p = 0.021  

## Backtest (2010 on, walk-forward): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45629.0    0.5123  0.2500      -0.0011
momentum   45629.0    0.5105  0.2501      -0.0016
gbm        45629.0    0.5173  0.2505      -0.0030
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.189  
gbm vs base_rate: Brier gain per day -0.00047, p = 0.110  

## Backtest (2010 on, walk-forward): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46519.0    0.5403  0.2486      -0.0022
momentum   46519.0    0.5362  0.2486      -0.0023
gbm        46519.0    0.5366  0.2490      -0.0040
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.845  
gbm vs base_rate: Brier gain per day -0.00044, p = 0.052  

## Backtest (2010 on, walk-forward): calm

```
                 n  hit_rate   brier  brier_skill
base_rate  81731.0    0.5237  0.2494      -0.0009
momentum   81731.0    0.5202  0.2495      -0.0011
gbm        81731.0    0.5246  0.2499      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00005, p = 0.458  
gbm vs base_rate: Brier gain per day -0.00036, p = 0.055  

## Backtest (2010 on, walk-forward): stressed

```
                 n  hit_rate   brier  brier_skill
base_rate  10417.0    0.5473  0.2479      -0.0037
momentum   10417.0    0.5491  0.2481      -0.0045
gbm        10417.0    0.5460  0.2484      -0.0056
```
momentum vs base_rate: Brier gain per day -0.00022, p = 0.216  
gbm vs base_rate: Brier gain per day -0.00020, p = 0.789  

## GBM calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]   1962     0.407     0.531
(0.45, 0.5]   8659     0.485     0.514
(0.5, 0.55]  73659     0.527     0.533
(0.55, 0.6]   7601     0.560     0.532
(0.6, 1.0]     267     0.632     0.536
```

## Latest forecasts: P(up over next 2 trading days), 22 new rows logged

```
                            date  base_rate  momentum    gbm
market ticker                                               
US     ^GSPC          2026-10-28      0.556     0.570  0.533
       AAPL           2026-10-28      0.541     0.551  0.533
       MSFT           2026-10-28      0.524     0.532  0.531
       NVDA           2026-10-28      0.533     0.543  0.531
       AMZN           2026-10-28      0.520     0.525  0.535
       GOOGL          2026-10-28      0.544     0.532  0.526
       JPM            2026-10-28      0.528     0.519  0.530
       XOM            2026-10-28      0.526     0.526  0.521
       JNJ            2026-10-28      0.528     0.533  0.528
       PG             2026-10-28      0.525     0.515  0.524
       WMT            2026-10-28      0.523     0.516  0.520
India  ^NSEI          2026-10-28      0.537     0.528  0.534
       RELIANCE.NS    2026-10-28      0.518     0.525  0.528
       HDFCBANK.NS    2026-10-28      0.518     0.532  0.524
       ICICIBANK.NS   2026-10-28      0.514     0.527  0.529
       INFY.NS        2026-10-28      0.520     0.517  0.517
       TCS.NS         2026-10-28      0.494     0.521  0.519
       BHARTIARTL.NS  2026-10-28      0.513     0.517  0.521
       ITC.NS         2026-10-28      0.515     0.517  0.525
       LT.NS          2026-10-28      0.521     0.508  0.514
       SBIN.NS        2026-10-28      0.520     0.511  0.532
       HINDUNILVR.NS  2026-10-28      0.510     0.527  0.527
```
