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
gbm        92148.0    0.5266  0.2497      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.182  
gbm vs base_rate: Brier gain per day -0.00047, p = 0.020  

## Backtest (2010 on, walk-forward): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45629.0    0.5123  0.2500      -0.0011
momentum   45629.0    0.5105  0.2501      -0.0016
gbm        45629.0    0.5172  0.2504      -0.0030
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.189  
gbm vs base_rate: Brier gain per day -0.00047, p = 0.113  

## Backtest (2010 on, walk-forward): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46519.0    0.5403  0.2486      -0.0022
momentum   46519.0    0.5362  0.2486      -0.0023
gbm        46519.0    0.5358  0.2490      -0.0041
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.845  
gbm vs base_rate: Brier gain per day -0.00046, p = 0.045  

## Backtest (2010 on, walk-forward): calm

```
                 n  hit_rate   brier  brier_skill
base_rate  81731.0    0.5237  0.2494      -0.0009
momentum   81731.0    0.5202  0.2495      -0.0011
gbm        81731.0    0.5243  0.2499      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00005, p = 0.458  
gbm vs base_rate: Brier gain per day -0.00036, p = 0.059  

## Backtest (2010 on, walk-forward): stressed

```
                 n  hit_rate   brier  brier_skill
base_rate  10417.0    0.5473  0.2479      -0.0037
momentum   10417.0    0.5491  0.2481      -0.0045
gbm        10417.0    0.5449  0.2485      -0.0059
```
momentum vs base_rate: Brier gain per day -0.00022, p = 0.216  
gbm vs base_rate: Brier gain per day -0.00026, p = 0.730  

## GBM calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]   1982     0.407     0.534
(0.45, 0.5]   8605     0.485     0.516
(0.5, 0.55]  73672     0.527     0.532
(0.55, 0.6]   7627     0.561     0.534
(0.6, 1.0]     262     0.632     0.527
```

## Latest forecasts: P(up over next 2 trading days), 22 new rows logged

```
                            date  base_rate  momentum    gbm     ai
market ticker                                                      
US     ^GSPC          2026-10-28      0.556     0.570  0.533  0.550
       AAPL           2026-10-28      0.541     0.551  0.534  0.530
       MSFT           2026-10-28      0.524     0.532  0.530  0.550
       NVDA           2026-10-28      0.533     0.543  0.532  0.520
       AMZN           2026-10-28      0.520     0.525  0.534  0.520
       GOOGL          2026-10-28      0.544     0.532  0.525  0.450
       JPM            2026-10-28      0.528     0.519  0.531  0.530
       XOM            2026-10-28      0.526     0.526  0.521  0.526
       JNJ            2026-10-28      0.528     0.533  0.528  0.540
       PG             2026-10-28      0.525     0.515  0.524  0.520
       WMT            2026-10-28      0.523     0.516  0.521  0.530
India  ^NSEI          2026-10-28      0.537     0.528  0.535  0.510
       RELIANCE.NS    2026-10-28      0.518     0.525  0.527  0.540
       HDFCBANK.NS    2026-10-28      0.518     0.532  0.523  0.518
       ICICIBANK.NS   2026-10-28      0.514     0.527  0.530  0.510
       INFY.NS        2026-10-28      0.520     0.517  0.518  0.460
       TCS.NS         2026-10-28      0.494     0.521  0.521  0.470
       BHARTIARTL.NS  2026-10-28      0.513     0.517  0.522  0.490
       ITC.NS         2026-10-28      0.515     0.517  0.525  0.480
       LT.NS          2026-10-28      0.521     0.508  0.516  0.540
       SBIN.NS        2026-10-28      0.520     0.511  0.533  0.520
       HINDUNILVR.NS  2026-10-28      0.510     0.527  0.527  0.520
```

## AI analyst (gemini-3.5-flash-lite): ok

- **^GSPC** 0.55 (15 headlines): The historical frequency of a 2-day rise is 0.556, and recent market returns show moderate positive short-term momentum (+0.28% over 1 day) despite mixed premarket futures and earnings commentary. Headlines about tech earnings and AI spending do not provide sufficient systematic macro shock to signi
- **AAPL** 0.53 (15 headlines): The historical 2-day frequency is around 0.541, with mild recent negative returns (-0.94% over 1 day) and a low market stress probability. Headlines show mixed institutional activity and upcoming Q4 earnings previews with some concerns on memory costs and valuation, but no overwhelming negative shoc
- **MSFT** 0.55 (15 headlines): Microsoft recently reported Q3 2026 earnings with strong Azure cloud growth that exceeded expectations and positive reception to its AI capex strategy, driving recent upward momentum despite broader market AI spending scrutiny.
- **NVDA** 0.52 (15 headlines): The recent headlines show a mix of positive developments such as major hardware supplies and a large strategic stake in SpaceX, balanced against negative reports like a DOJ probe and competitive sell ratings. Since these news items are largely already reflected in the recent negative short-term mome
- **AMZN** 0.52 (15 headlines): The historical frequency of a rise over 2 days is 0.52, and while there are earnings announcements upcoming, the market is largely anticipating these results without a clear directional shock already priced in, leaving the probability close to the historical baseline.
- **GOOGL** 0.45 (15 headlines): Google stock experienced a significant post-earnings sell-off and plunge following a Q3 2026 earnings miss and search slowdown concerns. While some analysts view the pullback as a buying opportunity, the immediate negative sentiment and heavy downside momentum from the earnings miss warrant adjustin
- **JPM** 0.53 (15 headlines): The recent headlines reflect routine institutional buying/selling, analyst target adjustments, and general commentary that do not provide major unexpected catalysts or earnings surprises not already absorbed by the market. Consequently, the probability remains very close to the historical 2-day upwa
- **XOM** 0.53 (15 headlines): The historical 2-day frequency for XOM is 0.526. Recent headlines primarily discuss incoming Q3 earnings, analyst ratings adjustments, and institutional position changes, which do not provide sufficient macro or fundamental surprises to justify a significant departure from the baseline historical pr
- **JNJ** 0.54 (15 headlines): Recent headlines show positive catalysts including raised 2026 revenue guidance, strong Q3 growth reports, and inclusion in healthcare fund buying, which slightly tilts the short-term probability above the historical baseline of 0.528 while remaining within a well-calibrated range.
- **PG** 0.52 (15 headlines): The historical frequency of a 2-day rise is 0.525, and recent news regarding earnings, analyst rating adjustments, and valuation discussions are mixed without presenting an overwhelming directional shock not already absorbed by prices, keeping the probability close to the base rate.
- **WMT** 0.53 (15 headlines): Historical 2-day frequency is slightly above 50 percent, and recent news shows positive developments such as healthcare platform expansion and net ETF buying outweighing regulatory inquiries and routine insider/institutional transactions, supporting a mild upward bias.
- **^NSEI** 0.51 (15 headlines): The historical 2-day upward frequency is around 53.7%. Recent headlines indicate downward pressure due to surging oil prices and cautious global cues, which is slightly tempered by stabilizing factors like steady support levels and Fed rate holds. Factoring in these headwinds, a slight downward adju
- **RELIANCE.NS** 0.54 (15 headlines): The historical frequency of a 2-day rise is 0.518, and recent negative momentum is partially counterbalanced by significant positive news regarding the successful blockbuster listing and debut of Jio Platforms, which boosted Reliance's overall market valuation and conglomerate standing.
- **HDFCBANK.NS** 0.52 (15 headlines): The headlines show ongoing commentary regarding recent earnings, new leadership under Anup Bagchi, and analyst target price adjustments, but no major brand-new material surprises that the recent price action has not largely absorbed. Therefore, sticking close to the historical 2-day upward frequency
- **ICICIBANK.NS** 0.51 (15 headlines): The historical frequency of a 2-day rise is around 0.514. Recent headlines regarding ICICI Bank include positive long-term broker picks and dividend announcements, but also minor recent pullbacks in share price. There is no major unexpected earnings or macro shock that significantly deviates from no
- **INFY.NS** 0.46 (15 headlines): Infosys recently experienced multiple analyst downgrades and a significant share price drop following a guidance cut for FY27 and negative sentiment in IT stocks driven by AI capex concerns. While much of this bad news is priced in through the recent sharp decline, the heavy negative momentum and mu
- **TCS.NS** 0.47 (15 headlines): The recent headlines highlight heavy selling pressure in IT stocks due to the Anthropic IPO and Jio's stellar listing pushing TCS out of India's top five most valuable firms, accompanied by a sharp price drop of over 3%. Although short-term oversold conditions can sometimes trigger a minor rebound, 
- **BHARTIARTL.NS** 0.49 (15 headlines): Bharti Airtel recently faced a minor sell-off of over 2.6% due to the massive blockbuster debut and IPO listing of Jio Platforms, which temporarily surpassed Airtel in market capitalization. While medium-term momentum remains positive, the short-term negative sentiment from the headline-grabbing eve
- **ITC.NS** 0.48 (15 headlines): Although there is positive news regarding the strong Q2 earnings beat for ITC Hotels, the parent stock ITC recently hit a fresh 52-week low with concerns over potential higher cigarette taxes, leading to negative short-term momentum (-2.15% over 20 days) that slightly dampens the probability of an i
- **LT.NS** 0.54 (15 headlines): LT reported strong Q2 results with a 33% profit rise, robust order inflows, and positive brokerage upgrades, which provides fundamental support. However, since the stock surged significantly on the day of the news, short-term profit-taking or consolidation is likely, keeping the probability close to
- **SBIN.NS** 0.52 (15 headlines): The historical frequency of a 2-day rise is 0.520. While there are several news items, including an institutional purchase of shares and minor corporate developments, they do not present surprising material mispricings or significant shocks that would warrant a major departure from the baseline hist
- **HINDUNILVR.NS** 0.52 (15 headlines): Hindustan Unilever reported strong Q2 FY27 results with sales growth reaching a 14-quarter high and declared an interim dividend, though the stock fell slightly on inflation warnings and profit-taking. These fundamental positive factors slightly improve the short-term outlook above the historical ba
