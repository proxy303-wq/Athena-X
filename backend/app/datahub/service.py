from app.assets.registry import Asset
from app.groww.market import GrowwMarketService


class DataHub:

    @staticmethod
    def load(asset: Asset):

        quote = GrowwMarketService.get_quote(asset)

        candles = GrowwMarketService.get_historical(asset)

        return {
            "quote": quote,
            "candles": candles
        }