import pandas as pd


def make_lagged_features(frame, lags=96, horizon=96):
    if lags < 1 or horizon < 1:
        raise ValueError("lags and horizon must be positive")
    demand = frame["demand_kw"].reset_index(drop=True)
    columns = {f"lag_{i}": demand.shift(i) for i in range(1, lags + 1)}
    x = pd.DataFrame(columns)
    x["temperature_c"] = frame["temperature_c"].reset_index(drop=True)
    y = demand.shift(-horizon).rename("target")
    data = pd.concat([x, y], axis=1).dropna()
    return data.drop(columns="target"), data["target"]
