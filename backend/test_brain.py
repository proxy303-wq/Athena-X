from app.assets.registry import get_asset

from app.options.service import OptionService
from app.options.parser import OptionParser

from app.analytics.pipeline import AnalyticsPipeline

from app.brain.engine import AthenaBrain

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

analysis = AnalyticsPipeline.run(chain)

brain = AthenaBrain.think(analysis)

print()

print(brain)