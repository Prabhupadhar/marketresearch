# marketresearch

A self-scoring AI market analyst for US and Indian stocks. The goal and the bar to beat are in [GOAL.md](GOAL.md).

- **Code** lives on the default branch and changes only through pull requests.
- **Results** live on the `results` branch: `forecasts/log.csv` (append-only, every forecast logged before its outcome) and `reports/layer1.md`. The [loop workflow](.github/workflows/loop.yml) updates it after every trading day.

```bash
pip install -r requirements.txt
python test_layer1.py   # look-ahead, scoring math, append-only log
python layer1.py        # appends to forecasts/log.csv, writes reports/layer1.md
```
