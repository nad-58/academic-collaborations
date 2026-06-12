"""Optional LSTM model. Install TensorFlow separately to use this module."""


def build_lstm(input_steps: int, units: int = 32):
    try:
        from tensorflow import keras
    except ImportError as exc:
        raise ImportError("Install TensorFlow to use the optional LSTM model") from exc

    model = keras.Sequential([
        keras.layers.Input(shape=(input_steps, 1)),
        keras.layers.LSTM(units),
        keras.layers.Dense(1),
    ])
    model.compile(optimizer="adam", loss="mae")
    return model
