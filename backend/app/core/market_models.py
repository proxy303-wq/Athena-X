from pydantic import BaseModel


class OHLC(BaseModel):
    open: float
    high: float
    low: float
    close: float


class MarketQuote(BaseModel):
    symbol: str

    last_price: float

    day_change: float

    day_change_percent: float

    ohlc: OHLC

    week52_high: float

    week52_low: float