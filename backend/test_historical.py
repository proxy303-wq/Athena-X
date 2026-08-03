from pprint import pprint

from app.assets.registry import get_asset
from app.groww.market import GrowwMarketService

print("=" * 60)
print("ATHENA X - HISTORICAL CANDLES TEST")
print("=" * 60)

asset = get_asset("NIFTY")

data = GrowwMarketService.get_historical(asset)

print("\nReturned Type:\n")
print(type(data))

print("\nReturned Data:\n")

pprint(data)