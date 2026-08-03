from app.assets.registry import get_asset

from app.datahub.service import DataHub

from app.analytics.pipeline import AnalyticsPipeline

from app.decision.service import DecisionEngine

from app.dashboard.models import DashboardResponse


class DashboardService:

    @staticmethod
    def load(symbol: str):

        asset = get_asset(symbol)

        market = DataHub.load(asset)

        analysis = AnalyticsPipeline.run(
            market
        )

        trade = DecisionEngine.calculate(
            analysis
        )

        return DashboardResponse(

            market=market["quote"],

            analysis=analysis,

            trade=trade

        )