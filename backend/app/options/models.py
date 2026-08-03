from typing import Optional

from pydantic import BaseModel


class Greeks(BaseModel):

    delta: float

    gamma: float

    theta: float

    vega: float

    rho: float

    iv: float


class Option(BaseModel):

    strike: float

    option_type: str

    trading_symbol: str

    ltp: float

    open_interest: int

    volume: int

    greeks: Greeks


class Strike(BaseModel):

    strike: float

    call: Optional[Option] = None

    put: Optional[Option] = None


class OptionChain(BaseModel):

    underlying: str

    spot_price: float

    expiry: str

    strikes: list[Strike]