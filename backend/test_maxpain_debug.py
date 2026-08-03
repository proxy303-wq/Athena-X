from app.assets.registry import get_asset
from app.options.service import OptionService
from app.options.parser import OptionParser
from app.options.maxpain import MaxPainEngine

asset = get_asset("NIFTY")

expiry = "2026-08-04"

raw = OptionService.get_option_chain(asset, expiry)

chain = OptionParser.parse(
    raw,
    asset.trading_symbol,
    expiry
)

result = MaxPainEngine.calculate(chain)

print("=" * 60)
print("MAX PAIN")
print("=" * 60)

print("Spot :", chain.spot_price)
print("Max Pain :", result.max_pain)
print("Distance :", round(chain.spot_price - result.max_pain, 2))
print("Total Loss :", f"{result.total_loss:,.0f}")