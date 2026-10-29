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
momentum   92148.0    0.5234  0.2493      -0.0012
gbm        92148.0    0.5267  0.2497      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.180  
gbm vs base_rate: Brier gain per day -0.00046, p = 0.024  

## Backtest (2010 on, walk-forward): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45629.0    0.5123  0.2500      -0.0011
momentum   45629.0    0.5105  0.2501      -0.0016
gbm        45629.0    0.5171  0.2504      -0.0029
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.189  
gbm vs base_rate: Brier gain per day -0.00044, p = 0.129  

## Backtest (2010 on, walk-forward): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46519.0    0.5403  0.2486      -0.0022
momentum   46519.0    0.5360  0.2486      -0.0023
gbm        46519.0    0.5362  0.2490      -0.0041
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.841  
gbm vs base_rate: Brier gain per day -0.00046, p = 0.046  

## Backtest (2010 on, walk-forward): calm

```
                 n  hit_rate   brier  brier_skill
base_rate  81731.0    0.5237  0.2494      -0.0009
momentum   81731.0    0.5201  0.2495      -0.0011
gbm        81731.0    0.5245  0.2499      -0.0026
```
momentum vs base_rate: Brier gain per day -0.00005, p = 0.456  
gbm vs base_rate: Brier gain per day -0.00034, p = 0.073  

## Backtest (2010 on, walk-forward): stressed

```
                 n  hit_rate   brier  brier_skill
base_rate  10417.0    0.5473  0.2479      -0.0037
momentum   10417.0    0.5491  0.2481      -0.0045
gbm        10417.0    0.5444  0.2485      -0.0060
```
momentum vs base_rate: Brier gain per day -0.00022, p = 0.215  
gbm vs base_rate: Brier gain per day -0.00033, p = 0.663  

## GBM calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]   1938     0.407     0.529
(0.45, 0.5]   8639     0.485     0.516
(0.5, 0.55]  73542     0.527     0.533
(0.55, 0.6]   7799     0.561     0.533
(0.6, 1.0]     230     0.635     0.522
```

## Latest forecasts: P(up over next 2 trading days), 0 new rows logged

```
                            date  base_rate  momentum    gbm  ai
market ticker                                                   
US     ^GSPC          2026-10-28      0.556     0.570  0.534 NaN
       AAPL           2026-10-28      0.541     0.551  0.534 NaN
       MSFT           2026-10-28      0.524     0.532  0.531 NaN
       NVDA           2026-10-28      0.533     0.543  0.532 NaN
       AMZN           2026-10-28      0.520     0.525  0.534 NaN
       GOOGL          2026-10-28      0.544     0.532  0.525 NaN
       JPM            2026-10-28      0.528     0.519  0.530 NaN
       XOM            2026-10-28      0.526     0.526  0.522 NaN
       JNJ            2026-10-28      0.528     0.533  0.526 NaN
       PG             2026-10-28      0.525     0.515  0.527 NaN
       WMT            2026-10-28      0.523     0.516  0.522 NaN
India  ^NSEI          2026-10-28      0.537     0.528  0.535 NaN
       RELIANCE.NS    2026-10-28      0.518     0.525  0.528 NaN
       HDFCBANK.NS    2026-10-28      0.518     0.532  0.524 NaN
       ICICIBANK.NS   2026-10-28      0.514     0.527  0.530 NaN
       INFY.NS        2026-10-28      0.520     0.517  0.519 NaN
       TCS.NS         2026-10-28      0.494     0.521  0.523 NaN
       BHARTIARTL.NS  2026-10-28      0.513     0.517  0.523 NaN
       ITC.NS         2026-10-28      0.515     0.517  0.525 NaN
       LT.NS          2026-10-28      0.521     0.508  0.515 NaN
       SBIN.NS        2026-10-28      0.520     0.511  0.532 NaN
       HINDUNILVR.NS  2026-10-28      0.510     0.527  0.527 NaN
```

## AI analyst (gemini-3.8-flash): ^GSPC: TimeoutError; AAPL: TimeoutError; MSFT: TimeoutError; NVDA: TimeoutError; AMZN: TimeoutError; GOOGL: TimeoutError; JPM: TimeoutError; XOM: TimeoutError; JNJ: TimeoutError; PG: HTTPError 503; WMT: TimeoutError; ^NSEI: HTTPError 503; RELIANCE.NS: HTTPError 503; HDFCBANK.NS: TimeoutError; ICICIBANK.NS: HTTPError 503; INFY.NS: HTTPError 503; TCS.NS: HTTPError 503; BHARTIARTL.NS: TimeoutError; ITC.NS: HTTPError 503; LT.NS: TimeoutError; SBIN.NS: HTTPError 429; HINDUNILVR.NS: HTTPError 503

