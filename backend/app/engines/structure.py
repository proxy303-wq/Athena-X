from app.core.models import Evidence, Signal
from .base import BaseEngine


class StructureEngine(BaseEngine):

    name = "Market Structure"

    def analyze(self, context):

        df = context.candles.tail(10)

        highs = df["High"].tolist()
        lows = df["Low"].tolist()

        reasons = []

        bullish = highs[-1] > highs[-2] and lows[-1] > lows[-2]
        bearish = highs[-1] < highs[-2] and lows[-1] < lows[-2]

        if bullish:
            signal = Signal.BULLISH
            reasons.append("Higher High")
            reasons.append("Higher Low")

        elif bearish:
            signal = Signal.BEARISH
            reasons.append("Lower High")
            reasons.append("Lower Low")

        else:
            signal = Signal.NEUTRAL
            reasons.append("Sideways Market")

        return Evidence(
            engine=self.name,
            signal=signal,
            confidence=0.85,
            weight=0.25,
            reasons=reasons
        )