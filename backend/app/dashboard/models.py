from pydantic import BaseModel

from app.market.models import MarketSnapshot
from app.analytics.models import Analysis
from app.decision.models import TradePlan


class ChartCandle(BaseModel):

    time: int

    open: float
    high: float
    low: float
    close: float


class ChartPoint(BaseModel):

    time: int
    value: float


class ChartIndicators(BaseModel):

    ema20: list[ChartPoint]

    ema50: list[ChartPoint]

    vwap: list[ChartPoint]


class DashboardResponse(BaseModel):

    market: MarketSnapshot

    candles: list[ChartCandle]

    chart: ChartIndicators

    analysis: Analysis

    trade: TradePlan