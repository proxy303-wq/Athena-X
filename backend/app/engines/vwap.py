from app.core.models import Evidence, Signal
from app.indicators.service import IndicatorService

from .base import BaseEngine


class VWAPEngine(BaseEngine):

    name = "VWAP Engine"

    def analyze(self, context):

        df = context.candles.copy()

        # Yahoo returns zero volume for indices like NIFTY.
        # Use a placeholder volume so VWAP can still be computed.
        if (df["Volume"] == 0).all():
            df["Volume"] = 1

        df["VWAP"] = IndicatorService.vwap(df)

        latest = df.iloc[-1]

        if latest["Close"] > latest["VWAP"]:

            signal = Signal.BULLISH
            reasons = ["Price above VWAP"]

        elif latest["Close"] < latest["VWAP"]:

            signal = Signal.BEARISH
            reasons = ["Price below VWAP"]

        else:

            signal = Signal.NEUTRAL
            reasons = ["Price at VWAP"]

        return Evidence(
            engine=self.name,
            signal=signal,
            confidence=0.80,
            weight=0.20,
            reasons=reasons
        )