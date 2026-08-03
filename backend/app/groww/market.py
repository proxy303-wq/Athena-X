from datetime import datetime, timedelta

from app.assets.registry import Asset
from app.core.market_models import MarketQuote, OHLC
from app.core.candle_models import Candle, CandleSeries
from app.groww.client import groww


class GrowwMarketService:

    @staticmethod
    def get_quote(asset: Asset) -> MarketQuote:
        """
        Returns a typed MarketQuote object.
        """

        data = groww.get_quote(
            trading_symbol=asset.trading_symbol,
            exchange=asset.exchange,
            segment=asset.segment,
        )

        return MarketQuote(
            symbol=asset.trading_symbol,
            last_price=float(data["last_price"]),
            day_change=float(data["day_change"]),
            day_change_percent=float(data["day_change_perc"]),
            week52_high=float(data["week_52_high"]),
            week52_low=float(data["week_52_low"]),
            ohlc=OHLC(
                open=float(data["ohlc"]["open"]),
                high=float(data["ohlc"]["high"]),
                low=float(data["ohlc"]["low"]),
                close=float(data["ohlc"]["close"]),
            ),
        )

    @staticmethod
    def get_historical(
        asset: Asset,
        days: int = 5,
        interval: str = None,
    ) -> CandleSeries:
        """
        Returns historical candles as a typed CandleSeries.
        """

        if interval is None:
            interval = groww.CANDLE_INTERVAL_MIN_5

        end = datetime.now()
        start = end - timedelta(days=days)

        data = groww.get_historical_candles(
            exchange=asset.exchange,
            segment=asset.segment,
            groww_symbol=asset.groww_symbol,
            start_time=start.strftime("%Y-%m-%dT%H:%M:%S"),
            end_time=end.strftime("%Y-%m-%dT%H:%M:%S"),
            candle_interval=interval,
        )

        candles = []

        for row in data["candles"]:

            candles.append(
                Candle(
                    timestamp=datetime.fromisoformat(row[0]),
                    open=float(row[1]),
                    high=float(row[2]),
                    low=float(row[3]),
                    close=float(row[4]),
                    volume=float(row[5] or 0),
                )
            )

        return CandleSeries(
            symbol=asset.trading_symbol,
            timeframe=interval,
            candles=candles,
        )

    @staticmethod
    def get_option_chain(asset: Asset, expiry: str):
        """
        Returns raw option chain from Groww.
        We'll convert this into typed models later.
        """

        return groww.get_option_chain(
            exchange=asset.exchange,
            underlying=asset.trading_symbol,
            expiry_date=expiry,
        )