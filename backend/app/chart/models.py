from pydantic import BaseModel


class ChartPoint(BaseModel):
    time: int
    value: float


class ChartIndicators(BaseModel):

    ema20: list[ChartPoint]

    ema50: list[ChartPoint]

    vwap: list[ChartPoint]