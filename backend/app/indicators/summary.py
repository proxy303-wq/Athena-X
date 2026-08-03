from dataclasses import dataclass

from app.core.candle_models import CandleSeries

from app.indicators.ema import EMA
from app.indicators.rsi import RSI
from app.indicators.vwap import VWAP


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


class IndicatorService:

    @staticmethod
    def calculate(candles: CandleSeries) -> IndicatorSummary:

        ema20 = EMA.calculate(candles, 20)

        ema50 = EMA.calculate(candles, 50)

        rsi = RSI.calculate(candles)

        vwap = VWAP.calculate(candles)

        price = candles.candles[-1].close

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