from app.assets.registry import get_asset
from app.groww.market import GrowwMarketService

asset = get_asset("NIFTY")

series = GrowwMarketService.get_historical(asset)

print(type(series))
print()

print("Symbol:", series.symbol)
print("Timeframe:", series.timeframe)
print("Candles:", len(series.candles))

print("\nLatest Candle:\n")
print(series.candles[-1])