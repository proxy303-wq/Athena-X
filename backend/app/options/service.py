from app.assets.registry import Asset
from app.groww.client import groww


class OptionService:

    @staticmethod
    def get_expiries(asset: Asset, year=None, month=None):
        """
        Fetch available expiries from Groww.
        """

        return groww.get_expiries(
            exchange=asset.exchange,
            underlying_symbol=asset.trading_symbol,
            year=year,
            month=month,
        )

    @staticmethod
    def get_option_chain(asset: Asset, expiry: str):
        """
        Fetch complete option chain with Greeks.
        """

        return groww.get_option_chain(
            exchange=asset.exchange,
            underlying=asset.trading_symbol,
            expiry_date=expiry,
        )

    @staticmethod
    def get_greeks(asset: Asset, trading_symbol: str, expiry: str):
        """
        Fetch Greeks for a single option contract.
        """

        return groww.get_greeks(
            exchange=asset.exchange,
            underlying=asset.trading_symbol,
            trading_symbol=trading_symbol,
            expiry=expiry,
        )

    @staticmethod
    def get_first_working_chain(asset: Asset):
        """
        Automatically finds the first expiry that contains
        a non-empty option chain.
        """

        expiries = OptionService.get_expiries(asset)

        expiry_list = expiries.get("expiries", [])

        for expiry in expiry_list:

            raw = OptionService.get_option_chain(
                asset,
                expiry,
            )

            if raw.get("strikes"):
                return expiry, raw

        raise Exception("No option chain available.")