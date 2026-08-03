from pydantic import BaseModel


class OptionChainRow(BaseModel):
    strike: float

    call_ltp: float | None
    call_oi: int | None
    call_volume: int | None
    call_iv: float | None
    call_delta: float | None

    put_ltp: float | None
    put_oi: int | None
    put_volume: int | None
    put_iv: float | None
    put_delta: float | None

    is_atm: bool


class OptionChainResponse(BaseModel):
    spot: float
    expiry: str
    rows: list[OptionChainRow]