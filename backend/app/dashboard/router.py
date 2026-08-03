from fastapi import APIRouter, HTTPException

from app.dashboard.service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


@router.get("/{symbol}")
async def dashboard(symbol: str):
    try:
        return DashboardService.load(symbol.upper())
    except Exception as e:
        import traceback

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )