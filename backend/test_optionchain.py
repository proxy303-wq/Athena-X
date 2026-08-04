from app.assets.registry import get_asset
from app.options.service import OptionService
import json

asset = get_asset("NIFTY")

print("=" * 80)
print("ASSET")
print("=" * 80)
print(asset)

print()

print("=" * 80)
print("EXPIRIES")
print("=" * 80)

expiries = OptionService.get_expiries(asset)

expiry_list = expiries.get("expiries", [])

print(f"Found {len(expiry_list)} expiries")
print()

working_expiry = None

for expiry in expiry_list:

    print(f"Testing {expiry} ... ", end="")

    raw = OptionService.get_option_chain(
        asset,
        expiry,
    )

    strikes = raw.get("strikes", {})

    print(f"{len(strikes)} strikes")

    if len(strikes) > 0:
        working_expiry = expiry

        print()
        print("=" * 80)
        print(f"✅ FIRST WORKING EXPIRY : {expiry}")
        print("=" * 80)
        print()

        print(json.dumps(raw, indent=2))

        break

if working_expiry is None:

    print()
    print("❌ No expiry returned any option contracts.")