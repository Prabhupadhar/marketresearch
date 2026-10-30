# Layer 1 report

Horizon: 2 trading days.

## US regime (as of 2026-10-29)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.156    0.115       0.751     42.476  0.979
stressed      -0.221    0.296       0.249     13.510  0.021
```

## India regime (as of 2026-10-29)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.116    0.140       0.843    184.067  0.992
stressed      -0.103    0.372       0.157     28.190  0.008
```

## Forward scorecard

0 scored forecast dates so far; shown from 20.

## Backtest (2010 on, walk-forward): All

```
                 n  hit_rate   brier  brier_skill
base_rate  92160.0    0.5264  0.2493      -0.0009
momentum   92160.0    0.5235  0.2493      -0.0012
gbm        92160.0    0.5266  0.2497      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.177  
gbm vs base_rate: Brier gain per day -0.00046, p = 0.022  

## Backtest (2010 on, walk-forward): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45630.0    0.5123  0.2500      -0.0011
momentum   45630.0    0.5105  0.2501      -0.0016
gbm        45630.0    0.5172  0.2505      -0.0030
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.181  
gbm vs base_rate: Brier gain per day -0.00048, p = 0.099  

## Backtest (2010 on, walk-forward): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46530.0    0.5403  0.2486      -0.0022
momentum   46530.0    0.5362  0.2486      -0.0023
gbm        46530.0    0.5359  0.2490      -0.0040
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.836  
gbm vs base_rate: Brier gain per day -0.00043, p = 0.060  

## Backtest (2010 on, walk-forward): calm

```
                 n  hit_rate   brier  brier_skill
base_rate  81743.0    0.5238  0.2494      -0.0009
momentum   81743.0    0.5202  0.2495      -0.0011
gbm        81743.0    0.5242  0.2499      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00005, p = 0.449  
gbm vs base_rate: Brier gain per day -0.00036, p = 0.056  

## Backtest (2010 on, walk-forward): stressed

```
                 n  hit_rate   brier  brier_skill
base_rate  10417.0    0.5473  0.2479      -0.0037
momentum   10417.0    0.5491  0.2481      -0.0045
gbm        10417.0    0.5456  0.2484      -0.0058
```
momentum vs base_rate: Brier gain per day -0.00022, p = 0.216  
gbm vs base_rate: Brier gain per day -0.00026, p = 0.729  

## GBM calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]   1983     0.408     0.534
(0.45, 0.5]   8614     0.485     0.516
(0.5, 0.55]  73644     0.527     0.532
(0.55, 0.6]   7655     0.561     0.534
(0.6, 1.0]     264     0.631     0.534
```

## Latest forecasts: P(up over next 2 trading days), 48 new rows logged

```
                            date  base_rate  momentum    gbm     ai
market ticker                                                      
US     ^GSPC          2026-10-29      0.556     0.527  0.532  0.550
       AAPL           2026-10-29      0.541     0.551  0.530  0.541
       MSFT           2026-10-29      0.524     0.532  0.531  0.550
       NVDA           2026-10-29      0.533     0.514  0.531  0.520
       AMZN           2026-10-29      0.520     0.525  0.520  0.460
       GOOGL          2026-10-29      0.544     0.532  0.527  0.540
       JPM            2026-10-29      0.528     0.519  0.530  0.530
       XOM            2026-10-29      0.526     0.526  0.521  0.526
       JNJ            2026-10-29      0.528     0.533  0.528  0.530
       PG             2026-10-29      0.525     0.515  0.522  0.530
       WMT            2026-10-29      0.523     0.516  0.519  0.523
India  ^NSEI          2026-10-29      0.538     0.528  0.533  0.540
       RELIANCE.NS    2026-10-28      0.518     0.525  0.528  0.540
       HDFCBANK.NS    2026-10-28      0.518     0.532  0.524  0.510
       ICICIBANK.NS   2026-10-28      0.514     0.527  0.530  0.514
       INFY.NS        2026-10-28      0.520     0.517  0.518  0.480
       TCS.NS         2026-10-28      0.494     0.521  0.520  0.490
       BHARTIARTL.NS  2026-10-28      0.513     0.517  0.522  0.490
       ITC.NS         2026-10-28      0.515     0.517  0.525  0.470
       LT.NS          2026-10-28      0.521     0.508  0.515  0.580
       SBIN.NS        2026-10-28      0.520     0.511  0.532  0.520
       HINDUNILVR.NS  2026-10-28      0.510     0.527  0.527  0.450
```

## AI analyst (gemini-3.5-flash-lite): ok

- **^GSPC** 0.55 (15 headlines): The recent headlines reflect typical market noise, mild pullbacks from big tech earnings reactions (such as Alphabet and ServiceNow), and solid macroeconomic indicators like GDP beats. These do not present an extraordinary systemic shock that meaningfully departs from the historical two-day positive
- **AAPL** 0.54 (15 headlines): The recent headlines highlight strong performance, new product pricing, and an all-time closing high, but much of this positive momentum and recent gains (+1.48% in 1 day) are already reflected in the stock price. With no major unexpected shock or unabsorbed material earnings guidance yet released (
- **MSFT** 0.55 (15 headlines): Microsoft reported strong Q1 earnings with Azure growth surging 48% and profit jumping 32%, which eases some AI spending concerns and supports positive momentum despite initial post-earnings pullbacks and broader tech sector noise.
- **NVDA** 0.52 (15 headlines): The historical 2-day upward frequency for Nvidia is approximately 53.3%, and recent news headlines regarding political scrutiny, spy probes, and market cap competition do not constitute fundamentally new surprise earnings or macroeconomic policy shifts that would drastically alter the short-term tec
- **AMZN** 0.46 (15 headlines): Amazon reported Q3 earnings with heavy AI spending and revenue concerns causing an initial drop in the stock. While short-term earnings misses and tech sector pressure create negative sentiment, medium-term fundamentals and AWS growth suggest potential stabilization within two trading days.
- **GOOGL** 0.54 (15 headlines): Alphabet experienced a historic single-day drop of nearly 13 percent due to AI spending jitters and earnings concerns, which is fully reflected in the latest prices. While the sell-off is severe, historical mean-reversion tendencies and value-buying discussions suggest that the 2-day probability of 
- **JPM** 0.53 (15 headlines): The historical frequency of a rise over 2 days is 0.528, and recent positive momentum with a 1-day return of +1.26% supports a slight upward tilt, while headlines mainly consist of routine analyst rating adjustments and target price changes rather than major company-specific catalysts that would sig
- **XOM** 0.53 (15 headlines): The historical frequency for a 2-day rise is 0.526 and recent headlines concerning institutional holdings, upcoming Q3 earnings, and geopolitical tensions are largely expected and already reflected in the strong recent momentum (+11.88% over 20 days), keeping the probability near the base rate.
- **JNJ** 0.53 (15 headlines): The recent headlines are generally positive regarding Q3 performance and portfolio inclusion, but they do not contain surprising or transformative material news that is not already reflected in the recent upward price momentum (+2.84% over 5 days). Therefore, the estimate remains very close to the h
- **PG** 0.53 (15 headlines): Historical 2-day frequency is slightly above 50% at 0.525. Recent headlines regarding Q1 earnings, accelerating revenue, and rising costs are already largely absorbed by the recent market price action, including the 1.4% climb on October 29. With low market stress and solid momentum over the past 20
- **WMT** 0.52 (15 headlines): The recent headlines highlight strong operational updates including a 6 billion automation commitment with Symbotic, international rollout in Mexico, and partnership deals. However, much of this positive news and the +2.09% single-day gain on October 29 have already been absorbed by the market. Cons
- **^NSEI** 0.54 (15 headlines): The market recently gained over 1% with strong momentum and positive Q2 earnings sentiment, but ongoing concerns regarding oil prices and geopolitical tensions create conflicting signals, keeping the probability close to the historical baseline of 0.538.
- **RELIANCE.NS** 0.54 (15 headlines): Reliance Industries recently saw the historic debut of Jio Platforms with significant listing gains, and the company surpassed Tata Group to become India's biggest conglomerate by market valuation. Although there was some short-term pressure on the broader market due to oil prices, these major posit
- **HDFCBANK.NS** 0.51 (15 headlines): The stock recently experienced a decline, hitting 52-week lows, while new leadership under Anup Bagchi took charge and Q2 results were processed. Since recent price action reflects these factors, the probability remains close to the historical base rate.
- **ICICIBANK.NS** 0.51 (9 headlines): The recent headlines regarding stock option allotments, analyst target prices, and general market commentary do not contain material new surprises or fundamental shocks that would significantly deviate the short-term trajectory from its long-term historical 2-day frequency.
- **INFY.NS** 0.48 (15 headlines): Infosys shares dropped sharply by over 4% due to a guidance cut and broader sell-off in IT stocks amid AI trade concerns, but strong longer-term momentum and insider buying by Narayana Murthy's family office suggest some stabilization potential, keeping the probability slightly below the historical 
- **TCS.NS** 0.49 (15 headlines): The recent negative news regarding the IT sector drop, Anthropic IPO fears, and TCS falling out of the top 5 most valuable firms due to Jio's listing are already reflected in the recent negative returns (-1.48% over 1 day and -2.73% over 5 days). Despite strong 20-day momentum (+19.43%) and low prob
- **BHARTIARTL.NS** 0.49 (15 headlines): Bharti Airtel recently experienced a slight pullback due to the blockbuster IPO and high-profile market debut of Jio Platforms, which temporarily displaced Airtel as the second-most valuable company and largest telecom player by market capitalization. While the news is already partially priced in wi
- **ITC.NS** 0.47 (14 headlines): Although there is positive news regarding the recent Q2 results and rally of its spin-off ITC Hotels, the core ITC stock itself has hit a fresh 52-week low amid negative short-term momentum, declining 1-day, 5-day, and 20-day returns, and concerns over potential tax headwinds affecting its cigarette
- **LT.NS** 0.58 (15 headlines): Larsen  Toubro shares surged following very strong Q2 results, upbeat broker target upgrades, and long-term order book expansion plans. Although some gains are already priced in, the wave of strong fundamental news and positive analyst revisions slightly tilts the short-term probability above the hi
- **SBIN.NS** 0.52 (15 headlines): The historical frequency of a 2-day rise is 0.520. While there are various headlines regarding SBI climbing in rankings following Jio's listing, institutional share purchases by ICICI Lombard, and minor data breach assurance statements alongside some bearish technical momentum, these news items do n
- **HINDUNILVR.NS** 0.45 (15 headlines): HUL reported Q2 earnings with strong sales growth and dividend announcements, but the stock fell significantly towards 52-week lows due to margin pressures, inflation warnings, and rising input costs. While some brokerages remain bullish on long-term volume recovery, the immediate negative price rea
