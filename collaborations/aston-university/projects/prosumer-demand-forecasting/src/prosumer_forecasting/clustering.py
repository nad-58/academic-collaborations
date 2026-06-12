from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


def cluster_features(frame, clusters=4):
    cols = [name for name in frame.columns if name.startswith("sf")]
    values = MinMaxScaler().fit_transform(frame[cols])
    output = frame.copy()
    output["cluster"] = KMeans(n_clusters=clusters, random_state=42, n_init=10).fit_predict(values)
    return output
