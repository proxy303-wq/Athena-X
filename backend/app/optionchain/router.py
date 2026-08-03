from fastapi import APIRouter

from app.groww.client import groww

router = APIRouter(
    prefix="/optionchain",
    tags=["Option Chain"],
)


@router.get("/{symbol}")
def option_chain(symbol: str):

    try:
        groww.client

        return {
            "authenticated": True
        }

    except Exception as e:

        return {
            "authenticated": False,
            "error": str(e),
            "type": type(e).__name__,
        }