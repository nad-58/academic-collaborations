from __future__ import annotations

import numpy as np
import pandas as pd


def clean_and_resample(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"timestamp", "demand_kw", "temperature_c"}
    if not required.issubset(frame.columns):
        raise ValueError(f"missing columns: {sorted(required - set(frame.columns))}")
    data = frame.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data = data.drop_duplicates("timestamp").sort_values("timestamp").set_index("timestamp")
    data.loc[data["demand_kw"] <= 0, "demand_kw"] = np.nan
    data["demand_kw"] = data["demand_kw"].interpolate(limit=8).ffill().bfill()
    data["temperature_c"] = data["temperature_c"].interpolate().ffill().bfill()
    data = data.resample("15min").mean().interpolate()
    data["demand_kw"] = data["demand_kw"].rolling(5, center=True, min_periods=1).mean()
    return data.reset_index()


def minmax_scale(values: pd.Series) -> pd.Series:
    low, high = float(values.min()), float(values.max())
    if np.isclose(high, low):
        return pd.Series(np.zeros(len(values)), index=values.index, dtype=float)
    return (values - low) / (high - low)
