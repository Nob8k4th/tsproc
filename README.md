# tsproc

`tsproc` 是一个不依赖 pandas 的时间序列处理小库，聚焦基础聚合、平滑和异常检测。

## 模块能力

- `TimeSeries`：以键值形式保存序列并按时间戳取值
- `Resampler`：支持 mean/sum/max/min 聚合
- `Smoother`：提供 SMA、EMA 两类平滑
- `Detector`：阈值检测与 Z-Score 检测

## 快速使用

```bash
pip install -e .
```

```python
from tsproc import TimeSeries, Resampler, Smoother, Detector

ts = TimeSeries({"2026-01-01T00:00:00": 10, "2026-01-01T01:00:00": 12})
print(ts.get("2026-01-01T00:00:00"))

values = [1, 2, 3, 20]
print(Resampler().aggregate(values, "mean"))
print(Smoother().sma(values, 2))
print(Detector().threshold_detect(values, 10))
```

## 测试

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest tests/ -v --tb=short --json-report --json-report-file=test_results.json
```
