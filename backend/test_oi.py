from app.assets.registry import get_asset
from app.options.service import OptionService
from app.options.parser import OptionParser
from app.options.atm import ATMEngine
from app.options.oi import OIEngine

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

atm = ATMEngine.calculate(chain)

oi = OIEngine.calculate(
    chain,
    atm
)

print("\n==========================")
print("SUPPORT / RESISTANCE")
print("==========================")

print("Support :", oi.support)
print("Resistance :", oi.resistance)

print("\n==========================")
print("TOP CALL WRITING")
print("==========================")

for level in oi.top_call_writers:

    print(
        f"Strike {level.strike} | "
        f"Call OI={level.call_oi:,} | "
        f"Call Volume={level.call_volume:,}"
    )

print("\n==========================")
print("TOP PUT WRITING")
print("==========================")

for level in oi.top_put_writers:

    print(
        f"Strike {level.strike} | "
        f"Put OI={level.put_oi:,} | "
        f"Put Volume={level.put_volume:,}"
    )