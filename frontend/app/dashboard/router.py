from fastapi import APIRouter

from app.dashboard.service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/{symbol}")

def dashboard(symbol: str):

    return DashboardService.load(symbol)