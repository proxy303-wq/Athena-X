from enum import Enum

from pydantic import BaseModel


class Signal(str, Enum):
    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"


class Evidence(BaseModel):

    engine: str

    signal: Signal

    confidence: float

    weight: float

    reasons: list[str]