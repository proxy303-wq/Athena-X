from pprint import pprint

from app.assets.registry import get_asset
from app.options.service import OptionService

print("=" * 80)
print("ATHENA X - OPTION CHAIN TEST")
print("=" * 80)

asset = get_asset("NIFTY")

expiries = OptionService.get_expiries(asset)

print("\nAvailable Expiries:\n")

for i, expiry in enumerate(expiries["expiries"]):
    print(i, expiry)

# Use August expiry instead of January
expiry = "2026-08-04"

print("\nUsing Expiry:", expiry)

chain = OptionService.get_option_chain(
    asset,
    expiry
)

print("\nReturned Type:")
print(type(chain))

print("\nUnderlying LTP:")
print(chain.get("underlying_ltp"))

print("\nNumber of Strikes:")
print(len(chain.get("strikes", {})))

print("\nFirst 5 Strikes:")

strikes = list(chain.get("strikes", {}).keys())

print(strikes[:5])

if strikes:
    print("\nFirst Strike Data:\n")
    pprint(chain["strikes"][strikes[0]])