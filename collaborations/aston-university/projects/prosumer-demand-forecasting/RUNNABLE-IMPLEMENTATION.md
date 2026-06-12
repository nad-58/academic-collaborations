# Runnable Python Implementation

This project contains a synthetic-data example of short-term electricity demand forecasting.

## Modules

- synthetic data generation
- cleaning and 15-minute resampling
- seven daily shape factors
- lagged day-ahead features
- k-means clustering
- profile aggregation
- linear regression and random forest benchmarks
- optional LSTM architecture

See [Architecture and Technical Insights](ARCHITECTURE-AND-INSIGHTS.md) for the smart-grid model triad, five-stage pipeline, cluster-routing design, and aggregation effect.

## Install and run

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python examples/run_pipeline.py
python -m pytest -q
```

The implementation uses generated data and is intended for education and portfolio demonstration.
