# Layer 1 report

Horizon: 2 trading days.

## US regime (as of 2026-10-30)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.155    0.115       0.752       42.5  0.978
stressed      -0.221    0.296       0.248       13.5  0.022
```

## India regime (as of 2026-10-30)

```
          ann_return  ann_vol  time_share  avg_weeks    now
calm           0.116    0.140       0.843    184.092  0.991
stressed      -0.103    0.372       0.157     28.190  0.009
```

## Forward scorecard

1 scored forecast dates so far; shown from 20.

## Backtest (2010 on, walk-forward): All

```
                 n  hit_rate   brier  brier_skill
base_rate  92192.0    0.5265  0.2493      -0.0009
momentum   92192.0    0.5234  0.2493      -0.0012
gbm        92192.0    0.5262  0.2497      -0.0027
```
momentum vs base_rate: Brier gain per day -0.00008, p = 0.177  
gbm vs base_rate: Brier gain per day -0.00045, p = 0.027  

## Backtest (2010 on, walk-forward): India

```
                 n  hit_rate   brier  brier_skill
base_rate  45651.0    0.5124  0.2500      -0.0011
momentum   45651.0    0.5106  0.2501      -0.0016
gbm        45651.0    0.5166  0.2504      -0.0029
```
momentum vs base_rate: Brier gain per day -0.00013, p = 0.188  
gbm vs base_rate: Brier gain per day -0.00044, p = 0.130  

## Backtest (2010 on, walk-forward): US

```
                 n  hit_rate   brier  brier_skill
base_rate  46541.0    0.5403  0.2486      -0.0022
momentum   46541.0    0.5360  0.2486      -0.0023
gbm        46541.0    0.5357  0.2490      -0.0040
```
momentum vs base_rate: Brier gain per day -0.00002, p = 0.827  
gbm vs base_rate: Brier gain per day -0.00044, p = 0.057  

## Backtest (2010 on, walk-forward): calm

```
                 n  hit_rate   brier  brier_skill
base_rate  81775.0    0.5238  0.2494      -0.0009
momentum   81775.0    0.5202  0.2495      -0.0011
gbm        81775.0    0.5240  0.2499      -0.0026
```
momentum vs base_rate: Brier gain per day -0.00005, p = 0.450  
gbm vs base_rate: Brier gain per day -0.00032, p = 0.090  

## Backtest (2010 on, walk-forward): stressed

```
                 n  hit_rate   brier  brier_skill
base_rate  10417.0    0.5473  0.2479      -0.0037
momentum   10417.0    0.5491  0.2481      -0.0045
gbm        10417.0    0.5435  0.2485      -0.0061
```
momentum vs base_rate: Brier gain per day -0.00022, p = 0.215  
gbm vs base_rate: Brier gain per day -0.00030, p = 0.688  

## GBM calibration (backtest, all)

```
                 n  forecast  observed
p                                     
(0.0, 0.45]   1940     0.407     0.530
(0.45, 0.5]   8844     0.485     0.518
(0.5, 0.55]  73544     0.527     0.533
(0.55, 0.6]   7619     0.561     0.532
(0.6, 1.0]     245     0.634     0.518
```

## Latest forecasts: P(up over next 2 trading days), 88 new rows logged

```
                            date  base_rate  momentum    gbm     ai
market ticker                                                      
US     ^GSPC          2026-10-30      0.556     0.527  0.549  0.540
       AAPL           2026-10-30      0.541     0.551  0.550  0.530
       MSFT           2026-10-30      0.524     0.531  0.541  0.530
       NVDA           2026-10-30      0.533     0.514  0.525  0.520
       AMZN           2026-10-30      0.520     0.525  0.532  0.480
       GOOGL          2026-10-30      0.544     0.531  0.539  0.544
       JPM            2026-10-30      0.528     0.519  0.548  0.528
       XOM            2026-10-30      0.526     0.526  0.532  0.530
       JNJ            2026-10-30      0.528     0.534  0.536  0.528
       PG             2026-10-30      0.525     0.515  0.532  0.520
       WMT            2026-10-30      0.524     0.516  0.523  0.530
India  ^NSEI          2026-10-30      0.538     0.528  0.533  0.540
       RELIANCE.NS    2026-10-30      0.518     0.525  0.524  0.580
       HDFCBANK.NS    2026-10-30      0.519     0.532  0.522  0.520
       ICICIBANK.NS   2026-10-30      0.514     0.527  0.523  0.520
       INFY.NS        2026-10-30      0.520     0.523  0.505  0.520
       TCS.NS         2026-10-30      0.494     0.521  0.505  0.540
       BHARTIARTL.NS  2026-10-30      0.513     0.513  0.519  0.510
       ITC.NS         2026-10-30      0.515     0.518  0.524  0.510
       LT.NS          2026-10-30      0.522     0.508  0.513  0.540
       SBIN.NS        2026-10-30      0.520     0.512  0.524  0.520
       HINDUNILVR.NS  2026-10-30      0.510     0.528  0.524  0.540
```

## AI analyst (gemini-3.5-flash-lite): ok

- **^GSPC** 0.54 (15 headlines): The market experienced a notable 1-day drop (-1.82%) and negative momentum heading into the weekend, alongside tech/AI selloff pressures highlighted in the news. However, historical two-day bounce tendencies remain relatively resilient, and most macroeconomic/earnings fundamentals do not indicate an
- **AAPL** 0.53 (15 headlines): Apple recently reclaimed the title of the world's most valuable company amid a broader tech and AI sell-off, with slight negative momentum (-1.23% in the last day) driven by insider selling and cautious near-term sentiment. While major headlines highlight market cap shifts and forthcoming earnings/m
- **MSFT** 0.53 (15 headlines): The recent headlines covering Microsoft's massive bond issuance and strong Azure growth are largely already absorbed by the market, and the short-term negative momentum (-1.55% over 1 day) is counterbalanced by strong structural cloud growth and general positive sentiment among analysts, keeping the
- **NVDA** 0.52 (15 headlines): The recent negative headlines reflect a tech selloff, Apple overtaking Nvidia in market cap, and a 4.2% drop on the last trading day, which are largely absorbed by the current price. While momentum is negative over 1, 5, and 20 days, short-term mean reversion and the historical 2-day frequency of 0.
- **AMZN** 0.48 (15 headlines): Recent headlines indicate heavy selling and negative market sentiment following Amazon's earnings miss and AI spending concerns on October 30, 2026. This near-term downward pressure slightly dampens the historical 2-day upward frequency.
- **GOOGL** 0.54 (15 headlines): The recent massive sell-off and historical drawdowns are largely captured in the price, and headlines reflect extreme negative sentiment and volatility rather than entirely new unpriced fundamental surprises. Consequently, staying close to the historical base frequency of 0.544 for a 2-day horizon i
- **JPM** 0.53 (15 headlines): The recent headlines largely consist of analyst price target adjustments for other equities and general rating changes, containing no direct, high-impact fundamental news specifically altering JPMorgan Chase  Co.'s own near-term earnings or macro outlook. Therefore, the estimate remains anchored to 
- **XOM** 0.53 (15 headlines): ExxonMobil reported strong Q3 earnings beats, dividend increases, and surging refining margins, but positive earnings surprises are typically priced in rapidly on the day of the release. With short-term returns already up and most 2-day moves acting as noise, the probability remains very close to th
- **JNJ** 0.53 (15 headlines): Recent headlines discuss recent all-time highs and mixed Q3 MedTech segment results, but no material new information has emerged that significantly deviates from the historical 2-day upward frequency of 0.528.
- **PG** 0.52 (15 headlines): The historical 2-day frequency is 0.525 and recent news shows mixed institutional adjustments alongside standard debt offerings and cost pressure discussions, none of which strongly shift the baseline near-term probability away from historical norms.
- **WMT** 0.53 (15 headlines): Walmart's strong recent momentum supported by a major 6B automation deal and new infrastructure investments creates a slight positive bias, though most 2-day moves remain close to the historical frequency.
- **^NSEI** 0.54 (15 headlines): The historical frequency of a 2-day rise is 0.538. Recent headlines show Nifty reclaiming the 23,000 mark and a positive Gift Nifty start pointing towards continuation, but mixed underlying breadth and standard noise keep the probability closely aligned with the long-term base rate.
- **RELIANCE.NS** 0.58 (15 headlines): Reliance Industries reported very strong Q2 results with net profit jumping significantly and beating estimates, alongside a stellar debut and strong earnings growth from Jio Platforms. This major positive fundamental news outweighs the short-term negative price momentum and increases the probabilit
- **HDFCBANK.NS** 0.52 (15 headlines): The recent headlines show a mix of routine institutional activities, ESOP allotments, and mild market fluctuations without any major unexpected structural shocks or extraordinary earnings surprises. The historical baseline frequency of 0.519 remains the most reliable anchor.
- **ICICIBANK.NS** 0.52 (15 headlines): The historical 2-day frequency of a rise is 0.514, supported by positive short-term momentum and favorable technical and analyst coverage headlines. There are no major negative surprises or stress regime indicators to warrant a significant departure from the base rate.
- **INFY.NS** 0.52 (15 headlines): The recent headlines regarding upcoming dividends, facility expansion, and IT sector rallies are generally positive but largely expected or absorbed by the strong 1-day (+3.36%) and 20-day (+19.20%) momentum. While there is a minor mention of a DOJ H-1B inquiry, it does not present new catastrophic 
- **TCS.NS** 0.54 (15 headlines): Recent news highlights positive analyst sentiment including Nomura maintaining a 'Buy' rating with a strong target price following management meetings, alongside reports of solid AI revenue growth projections and a broader recovery in IT stocks driven by sector-wide earnings beats. These catalysts m
- **BHARTIARTL.NS** 0.51 (15 headlines): The historical frequency of a 2-day rise is 0.513, and recent news regarding regulatory penalties, subscriber dynamics, and analyst ratings are mostly mixed and generally already absorbed by the market, keeping the probability close to the historical baseline.
- **ITC.NS** 0.51 (15 headlines): The historical frequency of a 2-day rise is around 0.515. Recent headlines indicate ITC shares are trading near 52-week lows ahead of upcoming Q2 earnings and November 2 results, while some reports note recent technical resilience (clearing the 20-day average) and hospitality expansion. These mixed 
- **LT.NS** 0.54 (15 headlines): Recent news highlights strong Q2 profit growth, significant new order wins including Dhaka Metro Rail contracts and Vyoma AI data center development, and inclusion in multiple Diwali brokerage picks. However, these positive catalysts are partially balanced by concerns regarding margin pressures note
- **SBIN.NS** 0.52 (15 headlines): The recent headlines regarding SBI include institutional stake acquisition, upcoming investor meetings, and positive reports on digital adoption and mutual fund AUM, offset slightly by short-term bearish technical shifts and marginal intraday slips. These pieces of news are broadly balanced and do n
- **HINDUNILVR.NS** 0.54 (15 headlines): Recent positive Q2 earnings results, strong analyst upgrades with forecasted upside, and upcoming dividend announcements provide positive near-term sentiment that slightly increases the probability of an upward move over the next two trading days relative to the historical baseline.
