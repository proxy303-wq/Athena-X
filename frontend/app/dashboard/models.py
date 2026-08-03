from pydantic import BaseModel

from app.market.models import MarketSnapshot
from app.analytics.models import Analysis
from app.decision.models import TradePlan


class DashboardResponse(BaseModel):

    market: MarketSnapshot

    analysis: Analysis

    trade: TradePlan