from app.assets.registry import get_asset

from app.options.service import OptionService
from app.options.parser import OptionParser

from app.analytics.pipeline import AnalyticsPipeline

from app.decision.service import DecisionEngine

asset = get_asset("NIFTY")

expiry="2026-08-04"

raw = OptionService.get_option_chain(
    asset,
    expiry
)

chain = OptionParser.parse(
    raw,
    asset.trading_symbol,
    expiry
)

analysis = AnalyticsPipeline.run(chain)

trade = DecisionEngine.calculate(analysis)

print()

print(trade)