from datetime import datetime

import pandas as pd
from pydantic import BaseModel


class MarketContext(BaseModel):
    symbol: str
    timeframe: str
    timestamp: datetime

    current_price: float

    candles: pd.DataFrame

    class Config:
        arbitrary_types_allowed = True