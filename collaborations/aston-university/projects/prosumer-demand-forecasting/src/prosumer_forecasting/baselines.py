import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score


def safe_mape(y_true, y_pred):
    actual = np.asarray(y_true, dtype=float)
    pred = np.asarray(y_pred, dtype=float)
    return float(np.mean(np.abs(actual - pred) / np.maximum(np.abs(actual), 1e-6)) * 100)


def _metric_dict(y_true, y_pred):
    return {
        "predictions": np.asarray(y_pred, dtype=float),
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "mape": safe_mape(y_true, y_pred),
        "r2": float(r2_score(y_true, y_pred)),
    }


def persistence_baseline(x_test, y_test, lag_column="lag_1"):
    if lag_column not in x_test.columns:
        raise ValueError(f"missing lag column: {lag_column}")
    return _metric_dict(y_test, x_test[lag_column].to_numpy())


def seasonal_naive_baseline(x_test, y_test, seasonal_lag=96):
    column = f"lag_{seasonal_lag}"
    if column not in x_test.columns:
        raise ValueError(f"missing seasonal lag column: {column}")
    return _metric_dict(y_test, x_test[column].to_numpy())


def benchmark_baselines(x_test, y_test, seasonal_lag=96):
    return {
        "persistence_lag_1": persistence_baseline(x_test, y_test),
        f"seasonal_naive_lag_{seasonal_lag}": seasonal_naive_baseline(x_test, y_test, seasonal_lag),
    }
