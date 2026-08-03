import pandas as pd


def calculate_vwap(df: pd.DataFrame) -> pd.Series:
    typical_price = (df["High"] + df["Low"] + df["Close"]) / 3

    cumulative_tp_volume = (typical_price * df["Volume"]).cumsum()
    cumulative_volume = df["Volume"].cumsum()

    return cumulative_tp_volume / cumulative_volume