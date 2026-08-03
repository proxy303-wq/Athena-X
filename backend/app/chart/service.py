from app.chart.indicators import ChartIndicatorEngine
from app.core.candle_models import CandleSeries


class ChartService:

    @staticmethod
    def build(candles: CandleSeries):

        return ChartIndicatorEngine.calculate(
            candles
        )