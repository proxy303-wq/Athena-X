from app.assets.registry import Asset
from app.groww.client import groww


class OptionService:

    @staticmethod
    def get_expiries(asset: Asset, year=None, month=None):

        return groww.get_expiries(
            exchange=asset.exchange,
            underlying_symbol=asset.trading_symbol,
            year=year,
            month=month,
        )

    @staticmethod
    def get_option_chain(asset: Asset, expiry: str):

        return groww.get_option_chain(
            exchange=asset.exchange,
            underlying=asset.trading_symbol,
            expiry_date=expiry,
        )

    @staticmethod
    def get_greeks(asset: Asset, trading_symbol: str, expiry: str):

        return groww.get_greeks(
            exchange=asset.exchange,
            underlying=asset.trading_symbol,
            trading_symbol=trading_symbol,
            expiry=expiry,
        )