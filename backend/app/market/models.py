from pydantic import BaseModel
from datetime import datetime


class MarketSnapshot(BaseModel):
    market: str
    price: float | None
    change: float | None
    change_percent: float | None
    high: float | None
    low: float | None
    open: float | None
    volume: int | None
    source: str
    timestamp: datetime