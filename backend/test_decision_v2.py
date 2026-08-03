from pprint import pprint

from app.assets.registry import get_asset
from app.datahub.service import DataHub
from app.options.service import OptionService
from app.options.parser import OptionParser
from app.analytics.pipeline import AnalyticsPipeline
from app.decision.service import DecisionEngine

asset = get_asset("NIFTY")

market = DataHub.load(asset)

expiries = OptionService.get_expiries(asset)
expiry = expiries["expiries"][-8]

raw = OptionService.get_option_chain(asset, expiry)

chain = OptionParser.parse(
    raw,
    asset.trading_symbol,
    expiry
)

analysis = AnalyticsPipeline.run(
    chain,
    market["candles"]
)

plan = DecisionEngine.calculate(analysis)

print()
print("=" * 70)
print("ATHENA X - DECISION ENGINE V2")
print("=" * 70)
print()

pprint(plan)