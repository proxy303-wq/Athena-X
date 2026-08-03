from app.core.models import Evidence, Signal
from app.indicators.service import IndicatorService

from .base import BaseEngine


class RSIEngine(BaseEngine):

    name = "RSI Engine"

    def analyze(self, context):

        df = context.candles.copy()

        df["RSI"] = IndicatorService.rsi(df)

        rsi = float(df["RSI"].iloc[-1])

        if rsi > 70:
            signal = Signal.BEARISH
            reasons = [f"RSI overbought ({rsi:.2f})"]

        elif rsi < 30:
            signal = Signal.BULLISH
            reasons = [f"RSI oversold ({rsi:.2f})"]

        else:
            signal = Signal.NEUTRAL
            reasons = [f"RSI neutral ({rsi:.2f})"]

        return Evidence(
            engine=self.name,
            signal=signal,
            confidence=0.80,
            weight=0.20,
            reasons=reasons,
        )