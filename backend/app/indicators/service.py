from dataclasses import dataclass

import pandas as pd

from app.core.candle_models import CandleSeries


# ============================================================
# Indicator Summary
# ============================================================

@dataclass
class IndicatorSummary:

    price: float

    ema20: float
    ema50: float

    rsi: float

    vwap: float

    price_above_ema20: bool

    ema20_above_ema50: bool

    price_above_vwap: bool


# ============================================================
# Indicator Service
# ============================================================

class IndicatorService:

    def __init__(self, series: CandleSeries):

        self.series = series

        self.df = pd.DataFrame([
            {
                "Open": candle.open,
                "High": candle.high,
                "Low": candle.low,
                "Close": candle.close,
                "Volume": candle.volume,
            }
            for candle in series.candles
        ])

    # --------------------------------------------------------
    # EMA
    # --------------------------------------------------------

    def ema(self, period: int):

        return (
            self.df["Close"]
            .ewm(span=period, adjust=False)
            .mean()
        )

    # --------------------------------------------------------
    # RSI
    # --------------------------------------------------------

    def rsi(self, period: int = 14):

        delta = self.df["Close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    # --------------------------------------------------------
    # VWAP
    # --------------------------------------------------------

    def vwap(self):

        typical_price = (
            self.df["High"]
            + self.df["Low"]
            + self.df["Close"]
        ) / 3

        # ----------------------------------------------------
        # Index instruments (NIFTY/BANKNIFTY/SENSEX)
        # Groww returns zero volume.
        # Use Typical Price as proxy.
        # ----------------------------------------------------

        if self.df["Volume"].sum() == 0:

            return typical_price

        # ----------------------------------------------------
        # Stocks / Commodities
        # ----------------------------------------------------

        cumulative_tp_volume = (
            typical_price * self.df["Volume"]
        ).cumsum()

        cumulative_volume = self.df["Volume"].cumsum()

        return cumulative_tp_volume / cumulative_volume

    # --------------------------------------------------------
    # Helpers
    # --------------------------------------------------------

    def latest_close(self):

        return float(self.df["Close"].iloc[-1])

    def latest_high(self):

        return float(self.df["High"].iloc[-1])

    def latest_low(self):

        return float(self.df["Low"].iloc[-1])

    def latest_volume(self):

        return float(self.df["Volume"].iloc[-1])

    # --------------------------------------------------------
    # Summary
    # --------------------------------------------------------

    def summary(self) -> IndicatorSummary:

        price = self.latest_close()

        ema20 = float(
            self.ema(20).iloc[-1]
        )

        ema50 = float(
            self.ema(50).iloc[-1]
        )

        rsi = float(
            self.rsi().iloc[-1]
        )

        vwap = float(
            self.vwap().iloc[-1]
        )

        return IndicatorSummary(

            price=price,

            ema20=ema20,

            ema50=ema50,

            rsi=rsi,

            vwap=vwap,

            price_above_ema20=price > ema20,

            ema20_above_ema50=ema20 > ema50,

            price_above_vwap=price > vwap,

        )