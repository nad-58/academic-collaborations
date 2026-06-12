import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def safe_mape(y_true, y_pred):
    actual = np.asarray(y_true, dtype=float)
    pred = np.asarray(y_pred, dtype=float)
    return float(np.mean(np.abs(actual - pred) / np.maximum(np.abs(actual), 1e-6)) * 100)


def evaluate(model, x_train, y_train, x_test, y_test):
    model.fit(x_train, y_train)
    pred = model.predict(x_test)
    return {"model": model, "predictions": pred, "mae": float(mean_absolute_error(y_test, pred)), "mape": safe_mape(y_test, pred), "r2": float(r2_score(y_test, pred))}


def benchmark_models(x_train, y_train, x_test, y_test):
    return {
        "linear_regression": evaluate(LinearRegression(), x_train, y_train, x_test, y_test),
        "random_forest": evaluate(RandomForestRegressor(n_estimators=80, random_state=42, n_jobs=-1), x_train, y_train, x_test, y_test),
    }
