from app.assets.registry import get_asset

from app.options.service import OptionService
from app.options.parser import OptionParser
from app.options.atm import ATMEngine
from app.options.greeks import GreeksEngine

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

greeks = GreeksEngine.calculate(
    chain,
    atm
)

print("=" * 60)
print("ATHENA - ATM GREEKS")
print("=" * 60)

print(greeks)