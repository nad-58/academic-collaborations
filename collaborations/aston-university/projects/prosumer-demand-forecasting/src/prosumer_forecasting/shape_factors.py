import numpy as np
import pandas as pd


def safe_ratio(a, b):
    return 0.0 if np.isclose(b, 0.0) else float(a / b)


def daily_shape_factors(frame):
    data = frame.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data["date"] = data["timestamp"].dt.date
    data["hour"] = data["timestamp"].dt.hour
    rows = []
    for date, day in data.groupby("date"):
        y = day["demand_kw"]
        office = day.loc[(day["hour"] >= 8) & (day["hour"] < 19), "demand_kw"]
        evening = day.loc[(day["hour"] >= 18) & (day["hour"] < 22), "demand_kw"]
        avg = float(y.mean())
        peak = float(y.max())
        rows.append({"date": date, "sf1": safe_ratio(avg, peak), "sf2": safe_ratio(float(office.mean()), peak), "sf3": safe_ratio(float(office.mean()), avg), "sf4": safe_ratio(float(evening.mean()), avg)})
    return pd.DataFrame(rows).fillna(0.0)
