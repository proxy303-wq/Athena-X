from fastapi import APIRouter

from .service import get_market_snapshot

router = APIRouter(
    prefix="/market",
    tags=["Market"],
)


@router.get("/")
def market():

    return get_market_snapshot()