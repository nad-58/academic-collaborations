# Runnable Python Implementation

This project contains a synthetic-data example of short-term electricity demand forecasting.

## Modules

- synthetic data generation
- cleaning and 15-minute resampling
- seven daily shape factors
- lagged day-ahead features
- k-means clustering
- profile aggregation
- persistence and seasonal-naive baselines
- linear regression and random forest benchmarks
- optional LSTM architecture

See [Architecture and Technical Insights](ARCHITECTURE-AND-INSIGHTS.md) for the smart-grid model triad, five-stage pipeline, cluster-routing design, and aggregation effect.

## Baseline-first evaluation

The benchmark now reports simple baselines before machine-learning models:

- `persistence_lag_1`: predicts the next value using the most recent observed lag.
- `seasonal_naive_lag_96`: predicts using the same quarter-hour period from the previous day.

These baselines provide a minimum performance reference. A more complex model should only be preferred if it improves on these simple alternatives under chronological validation.

## Install and run

```bash
python -m venv .venv
python -m pip install -e ".[dev]"
python examples/run_pipeline.py
python -m pytest -q
```

The implementation uses generated data and is intended for education and portfolio demonstration.
