from __future__ import annotations

import numpy as np
import pandas as pd


def make_synthetic_series(days: int = 60, seed: int = 42) -> pd.DataFrame:
    if days < 10:
        raise ValueError("days must be at least 10")
    rng = np.random.default_rng(seed)
    index = pd.date_range("2024-01-01", periods=days * 96, freq="15min")
    hour = index.hour.to_numpy() + index.minute.to_numpy() / 60
    morning = np.exp(-0.5 * ((hour - 7.5) / 1.2) ** 2)
    evening = np.exp(-0.5 * ((hour - 19.0) / 1.7) ** 2)
    weekend = np.where(index.dayofweek.to_numpy() >= 5, 1.15, 1.0)
    demand = np.clip((0.25 + 0.4 * morning + 0.75 * evening) * weekend + rng.normal(0, 0.05, len(index)), 0.03, None)
    temperature = 9 + 5 * np.sin(2 * np.pi * np.arange(len(index)) / (96 * 30))
    return pd.DataFrame({"timestamp": index, "demand_kw": demand, "temperature_c": temperature})
