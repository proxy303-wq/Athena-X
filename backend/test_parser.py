from app.assets.registry import get_asset
from app.options.parser import OptionParser
from app.options.service import OptionService

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

print(type(chain))

print()

print(chain.underlying)

print(chain.spot_price)

print()

print("Total Strikes:", len(chain.strikes))

print()

print(chain.strikes[0])

print()

print(chain.strikes[-1])