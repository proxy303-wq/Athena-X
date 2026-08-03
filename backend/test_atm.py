from app.assets.registry import get_asset
from app.options.parser import OptionParser
from app.options.service import OptionService
from app.options.atm import ATMEngine

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

print()

print(atm)