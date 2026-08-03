from app.core.models import Evidence, Signal
from app.indicators.service import IndicatorService

from .base import BaseEngine


class TrendEngine(BaseEngine):

    name = "Trend Engine"

    def analyze(self, context):

        df = context.candles.copy()

        # Calculate EMAs
        df["EMA20"] = IndicatorService.ema(df, 20)
        df["EMA50"] = IndicatorService.ema(df, 50)

        latest = df.iloc[-1]

        bullish_points = 0
        bearish_points = 0

        reasons = []

        # Rule 1
        if latest["Close"] > latest["EMA20"]:
            bullish_points += 1
            reasons.append("Price above EMA20")
        else:
            bearish_points += 1
            reasons.append("Price below EMA20")

        # Rule 2
        if latest["EMA20"] > latest["EMA50"]:
            bullish_points += 1
            reasons.append("EMA20 above EMA50")
        else:
            bearish_points += 1
            reasons.append("EMA20 below EMA50")

        total = bullish_points + bearish_points

        confidence = max(bullish_points, bearish_points) / total

        if bullish_points > bearish_points:
            signal = Signal.BULLISH
        elif bearish_points > bullish_points:
            signal = Signal.BEARISH
        else:
            signal = Signal.NEUTRAL

        return Evidence(
            engine=self.name,
            signal=signal,
            confidence=confidence,
            weight=0.30,
            reasons=reasons,
        )