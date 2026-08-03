from app.assets.registry import get_asset
from app.datahub.service import DataHub

asset = get_asset("NIFTY")

market = DataHub.load(asset)

print(type(market["quote"]))
print(type(market["candles"]))

print()

print(market["quote"])

print()

print(market["candles"].candles[-1])