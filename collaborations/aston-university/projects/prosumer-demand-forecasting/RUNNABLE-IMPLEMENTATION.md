# Runnable Python Implementation

This project contains a synthetic-data example of short-term electricity demand forecasting.

## Modules

- synthetic data generation
- cleaning and 15-minute resampling
- daily shape-factor features
- lagged day-ahead features
- k-means clustering
- linear regression and random forest benchmarks
- optional LSTM architecture

## Install and run

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python examples/run_pipeline.py
python -m pytest -q
```

The implementation uses generated data and is intended for education and portfolio demonstration.
