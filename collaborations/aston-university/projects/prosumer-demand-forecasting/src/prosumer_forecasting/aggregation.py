import pandas as pd


def aggregate_profiles(frames):
    if not frames:
        raise ValueError("at least one profile is required")
    series = []
    for index, frame in enumerate(frames):
        data = frame[["timestamp", "demand_kw"]].copy()
        data = data.rename(columns={"demand_kw": f"demand_{index}"})
        series.append(data)
    merged = series[0]
    for item in series[1:]:
        merged = merged.merge(item, on="timestamp", how="inner")
    demand_cols = [name for name in merged.columns if name.startswith("demand_")]
    merged["aggregate_demand_kw"] = merged[demand_cols].sum(axis=1)
    return merged[["timestamp", "aggregate_demand_kw"]]
