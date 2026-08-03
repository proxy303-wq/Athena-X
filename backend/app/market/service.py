from datetime import datetime

from .provider import get_nifty_data
from .models import MarketSnapshot


def get_market_snapshot():

    data = get_nifty_data()

    return MarketSnapshot(
        market="NIFTY",
        price=data["price"],
        change=None,
        change_percent=None,
        high=data["high"],
        low=data["low"],
        open=data["open"],
        volume=data["volume"],
        source="Yahoo Finance",
        timestamp=datetime.now(),
    )