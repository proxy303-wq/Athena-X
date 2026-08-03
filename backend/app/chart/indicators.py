import numpy as np
import pandas as pd

from app.chart.models import ChartPoint, ChartIndicators
from app.core.candle_models import CandleSeries


class ChartIndicatorEngine:

    @staticmethod
    def calculate(candles: CandleSeries) -> ChartIndicators:

        rows = []

        for candle in candles.candles:
            rows.append(
                {
                    "time": int(candle.timestamp.timestamp()),
                    "open": candle.open,
                    "high": candle.high,
                    "low": candle.low,
                    "close": candle.close,
                    "volume": candle.volume if candle.volume is not None else 0,
                }
            )

        df = pd.DataFrame(rows)

        # EMA20
        df["ema20"] = (
            df["close"]
            .ewm(span=20, adjust=False)
            .mean()
        )

        # EMA50
        df["ema50"] = (
            df["close"]
            .ewm(span=50, adjust=False)
            .mean()
        )

        # VWAP
        typical = (
            df["high"] +
            df["low"] +
            df["close"]
        ) / 3

        cumulative_volume = df["volume"].cumsum()

        df["vwap"] = np.where(
            cumulative_volume == 0,
            df["close"],
            (typical * df["volume"]).cumsum() / cumulative_volume,
        )

        return ChartIndicators(

            ema20=[
                ChartPoint(
                    time=int(r.time),
                    value=float(r.ema20),
                )
                for r in df.itertuples()
            ],

            ema50=[
                ChartPoint(
                    time=int(r.time),
                    value=float(r.ema50),
                )
                for r in df.itertuples()
            ],

            vwap=[
                ChartPoint(
                    time=int(r.time),
                    value=float(r.vwap),
                )
                for r in df.itertuples()
            ],

        )