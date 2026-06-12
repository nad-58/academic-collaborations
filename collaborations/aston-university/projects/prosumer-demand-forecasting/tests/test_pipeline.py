import numpy as np

from prosumer_forecasting.clustering import cluster_features
from prosumer_forecasting.lag_features import make_lagged_features
from prosumer_forecasting.models import safe_mape
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
    assert set(clustered["cluster"].unique()).issubset({0, 1})
    assert len(x) == len(y) and len(x) > 0
    assert np.isfinite(x.to_numpy()).all()


def test_scaling_and_mape_are_safe():
    scaled = minmax_scale(make_synthetic_series(days=10)["demand_kw"])
    assert scaled.min() >= 0 and scaled.max() <= 1
    assert np.isfinite(safe_mape([0.0, 1.0], [0.0, 0.8]))
