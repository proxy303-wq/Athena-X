from app.assets.registry import get_asset
from app.datahub.service import DataHub
from app.indicators.service import IndicatorService

asset = get_asset("NIFTY")

market = DataHub.load(asset)

ind = IndicatorService(
    market["candles"]
)

print()

print("EMA20")

print(ind.ema(20).iloc[-1])

print()

print("EMA50")

print(ind.ema(50).iloc[-1])

print()

print("RSI")

print(ind.rsi().iloc[-1])

print()

print("VWAP")

print(ind.vwap().iloc[-1])