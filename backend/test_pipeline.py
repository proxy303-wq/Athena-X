from pprint import pprint

from app.assets.registry import get_asset
from app.datahub.service import DataHub

from app.options.service import OptionService
from app.options.parser import OptionParser

from app.analytics.pipeline import AnalyticsPipeline


# ----------------------------------------------------------
# Asset
# ----------------------------------------------------------

asset = get_asset("NIFTY")

# ----------------------------------------------------------
# Market Data
# ----------------------------------------------------------

market = DataHub.load(asset)

candles = market["candles"]

# ----------------------------------------------------------
# Option Chain
# ----------------------------------------------------------

expiries = OptionService.get_expiries(asset)

expiry = expiries["expiries"][-8]

raw_chain = OptionService.get_option_chain(
    asset,
    expiry
)

chain = OptionParser.parse(
    raw_chain,
    asset.trading_symbol,
    expiry
)

# ----------------------------------------------------------
# Analytics
# ----------------------------------------------------------

analysis = AnalyticsPipeline.run(
    chain,
    candles
)

# ----------------------------------------------------------
# Output
# ----------------------------------------------------------

print()

print("=" * 70)
print("ATHENA X - ANALYTICS PIPELINE")
print("=" * 70)

print()

print("ATM")
pprint(analysis.atm)

print()

print("PCR")
pprint(analysis.pcr)

print()

print("OI")
pprint(analysis.oi)

print()

print("MAX PAIN")
pprint(analysis.max_pain)

print()

print("GREEKS")
pprint(analysis.greeks)

print()

print("INDICATORS")
pprint(analysis.indicators)