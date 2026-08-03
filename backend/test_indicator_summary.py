from app.assets.registry import get_asset
from app.datahub.service import DataHub
from app.indicators.service import IndicatorService

asset = get_asset("NIFTY")

market = DataHub.load(asset)

summary = IndicatorService(
    market["candles"]
).summary()

print(summary)