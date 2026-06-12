import numpy as np
import pandas as pd


def safe_ratio(a, b):
    return 0.0 if np.isclose(b, 0.0) else float(a / b)


def daily_shape_factors(frame):
    data = frame.copy()
    data["timestamp"] = pd.to_datetime(data["timestamp"])
    data["date"] = data["timestamp"].dt.date
    data["hour"] = data["timestamp"].dt.hour + data["timestamp"].dt.minute / 60
    rows = []
    for date, day in data.groupby("date"):
        y = day["demand_kw"]
        office = day.loc[(day["hour"] >= 8) & (day["hour"] < 19), "demand_kw"]
        lunch = day.loc[(day["hour"] >= 11) & (day["hour"] < 14), "demand_kw"]
        dinner = day.loc[(day["hour"] >= 18) & (day["hour"] < 22), "demand_kw"]
        night = day.loc[(day["hour"] >= 22) | (day["hour"] < 7), "demand_kw"]
        avg = float(y.mean())
        peak = float(y.max())
        office_avg = float(office.mean())
        rows.append({
            "date": date,
            "sf1": safe_ratio(avg, peak),
            "sf2": safe_ratio(office_avg, peak),
            "sf3": safe_ratio(office_avg, avg),
            "sf4": safe_ratio(float(lunch.mean()), avg),
            "sf5": safe_ratio(float(office.min()), office_avg),
            "sf6": safe_ratio(float(dinner.mean()), avg),
            "sf7": safe_ratio(float(night.max()) - float(dinner.max()), peak),
        })
    return pd.DataFrame(rows).fillna(0.0)
