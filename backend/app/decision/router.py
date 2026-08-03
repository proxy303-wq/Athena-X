from fastapi import APIRouter

from app.assets.registry import get_asset
from app.datahub.service import DataHub

from app.options.service import OptionService
from app.options.parser import OptionParser

from app.analytics.pipeline import AnalyticsPipeline
from app.decision.service import DecisionEngine

router = APIRouter(
    prefix="/decision",
    tags=["Decision"],
)


@router.get("/v2/{symbol}")
def decision_v2(symbol: str):

    asset = get_asset(symbol.upper())

    market = DataHub.load(asset)

    candles = market["candles"]

    expiries = OptionService.get_expiries(asset)

    expiry = expiries["expiries"][-8]

    raw = OptionService.get_option_chain(
        asset,
        expiry
    )

    chain = OptionParser.parse(
        raw,
        asset.trading_symbol,
        expiry
    )

    analysis = AnalyticsPipeline.run(
        chain,
        candles
    )

    plan = DecisionEngine.calculate(
        analysis
    )

    return {
        "analysis": analysis.model_dump(),
        "trade": plan.model_dump(),
    }