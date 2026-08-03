from app.assets.registry import get_asset
from app.options.service import OptionService
from app.options.parser import OptionParser
from app.options.maxpain import MaxPainEngine

asset = get_asset("NIFTY")

expiry = "2026-08-04"

raw = OptionService.get_option_chain(
    asset,
    expiry
)

chain = OptionParser.parse(
    raw,
    asset.trading_symbol,
    expiry
)

result = MaxPainEngine.calculate(chain)

print()

print(result)