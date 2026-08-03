from datetime import datetime

from app.assets.registry import get_asset
from app.datahub.service import DataHub

from app.options.service import OptionService
from app.options.parser import OptionParser

from app.analytics.pipeline import AnalyticsPipeline
from app.decision.service import DecisionEngine

from app.chart.service import ChartService

from app.dashboard.models import (
    DashboardResponse,
    ChartCandle,
    ChartIndicators,
    ChartPoint,
)

from app.market.models import MarketSnapshot


class DashboardService:

    @staticmethod
    def load(symbol: str):

        # ----------------------------------
        # Asset
        # ----------------------------------

        asset = get_asset(symbol)

        # ----------------------------------
        # Market
        # ----------------------------------

        market = DataHub.load(asset)

        quote = market["quote"]
        candles = market["candles"]

        # ----------------------------------
        # Option Chain
        # ----------------------------------

        expiries = OptionService.get_expiries(asset)

        expiry = expiries["expiries"][-8]

        raw_chain = OptionService.get_option_chain(
            asset,
            expiry,
        )

        chain = OptionParser.parse(
            raw_chain,
            asset.trading_symbol,
            expiry,
        )

        # ----------------------------------
        # Analytics
        # ----------------------------------

        analysis = AnalyticsPipeline.run(
            chain,
            candles,
        )

        # ----------------------------------
        # Chart Engine
        # ----------------------------------

        chart = ChartService.build(
            candles
        )

        # ----------------------------------
        # AI Decision
        # ----------------------------------

        trade = DecisionEngine.calculate(
            analysis
        )

        # ----------------------------------
        # Market Snapshot
        # ----------------------------------

        snapshot = MarketSnapshot(

            market=quote.symbol,

            price=quote.last_price,

            change=quote.day_change,

            change_percent=quote.day_change_percent,

            high=quote.ohlc.high,

            low=quote.ohlc.low,

            open=quote.ohlc.open,

            volume=None,

            source="Groww",

            timestamp=datetime.now(),

        )

        # ----------------------------------
        # Candles
        # ----------------------------------

        chart_candles = []

        candles.candles.sort(
            key=lambda c: c.timestamp
        )

        for candle in candles.candles:

            chart_candles.append(

                ChartCandle(

                    time=int(candle.timestamp.timestamp()),

                    open=candle.open,

                    high=candle.high,

                    low=candle.low,

                    close=candle.close,

                )

            )

        # ----------------------------------
        # Dashboard Response
        # ----------------------------------

        return DashboardResponse(

            market=snapshot,

            candles=chart_candles,

            chart=ChartIndicators(

                ema20=[
                    ChartPoint(
                        time=p.time,
                        value=p.value,
                    )
                    for p in chart.ema20
                ],

                ema50=[
                    ChartPoint(
                        time=p.time,
                        value=p.value,
                    )
                    for p in chart.ema50
                ],

                vwap=[
                    ChartPoint(
                        time=p.time,
                        value=p.value,
                    )
                    for p in chart.vwap
                ],

            ),

            analysis=analysis,

            trade=trade,

        )