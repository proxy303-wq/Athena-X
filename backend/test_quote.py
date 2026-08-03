from app.assets.registry import get_asset
from app.groww.market import GrowwMarketService

asset = get_asset("NIFTY")

quote = GrowwMarketService.get_quote(asset)

print(type(quote))
print(quote)