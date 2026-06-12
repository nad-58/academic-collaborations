from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from prosumer_forecasting.clustering import cluster_features
from prosumer_forecasting.lag_features import make_lagged_features
from prosumer_forecasting.models import benchmark_models
from prosumer_forecasting.preprocessing import clean_and_resample
from prosumer_forecasting.shape_factors import daily_shape_factors
from prosumer_forecasting.synthetic_data import make_synthetic_series


def main():
    data = clean_and_resample(make_synthetic_series())
    shapes = daily_shape_factors(data)
    clustered = cluster_features(shapes, clusters=4)
    x, y = make_lagged_features(data, lags=96, horizon=96)
    split = int(len(x) * 0.8)
    results = benchmark_models(x.iloc[:split], y.iloc[:split], x.iloc[split:], y.iloc[split:])
    print("Daily profiles:", len(clustered))
    print("Cluster counts:", clustered["cluster"].value_counts().sort_index().to_dict())
    for name, result in results.items():
        print(name, {key: round(result[key], 4) for key in ("mae", "mape", "r2")})


if __name__ == "__main__":
    main()
