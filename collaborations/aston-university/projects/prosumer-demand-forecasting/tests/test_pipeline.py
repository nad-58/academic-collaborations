import numpy as np
import pytest

from prosumer_forecasting.aggregation import aggregate_profiles
from prosumer_forecasting.baselines import benchmark_baselines, persistence_baseline, seasonal_naive_baseline
from prosumer_forecasting.clustering import cluster_features
from prosumer_forecasting.lag_features import make_lagged_features
from prosumer_forecasting.models import benchmark_models, safe_mape
from prosumer_forecasting.preprocessing import clean_and_resample, minmax_scale
from prosumer_forecasting.shape_factors import daily_shape_factors
from prosumer_forecasting.synthetic_data import make_synthetic_series


def test_public_pipeline_components():
    data = clean_and_resample(make_synthetic_series(days=20))
    shapes = daily_shape_factors(data)
    clustered = cluster_features(shapes, clusters=2)
    x, y = make_lagged_features(data, lags=8, horizon=4)
    assert len(data) == 20 * 96
    assert len(shapes) == 20
    assert {f"sf{i}" for i in range(1, 8)}.issubset(shapes.columns)
    assert set(clustered["cluster"].unique()).issubset({0, 1})
    assert len(x) == len(y) and len(x) > 0
    assert np.isfinite(x.to_numpy()).all()


def test_scaling_mape_and_aggregation():
    first = make_synthetic_series(days=10, seed=1)
    second = make_synthetic_series(days=10, seed=2)
    scaled = minmax_scale(first["demand_kw"])
    aggregate = aggregate_profiles([first, second])
    assert scaled.min() >= 0 and scaled.max() <= 1
    assert len(aggregate) == len(first)
    assert np.isfinite(aggregate["aggregate_demand_kw"]).all()
    assert np.isfinite(safe_mape([0.0, 1.0], [0.0, 0.8]))


def test_baseline_models_are_included():
    data = clean_and_resample(make_synthetic_series(days=18))
    x, y = make_lagged_features(data, lags=96, horizon=96)
    split = int(len(x) * 0.8)
    x_train, y_train = x.iloc[:split], y.iloc[:split]
    x_test, y_test = x.iloc[split:], y.iloc[split:]
    baselines = benchmark_baselines(x_test, y_test)
    results = benchmark_models(x_train, y_train, x_test, y_test)
    assert "persistence_lag_1" in baselines
    assert "seasonal_naive_lag_96" in baselines
    assert "persistence_lag_1" in results
    assert "seasonal_naive_lag_96" in results
    assert "random_forest" in results
    for item in results.values():
        assert np.isfinite(item["mae"])
        assert np.isfinite(item["mape"])
        assert np.isfinite(item["r2"])


def test_baselines_validate_required_lag_columns():
    data = clean_and_resample(make_synthetic_series(days=12))
    x, y = make_lagged_features(data, lags=8, horizon=4)
    with pytest.raises(ValueError):
        persistence_baseline(x.drop(columns=["lag_1"]), y)
    with pytest.raises(ValueError):
        seasonal_naive_baseline(x, y, seasonal_lag=96)
