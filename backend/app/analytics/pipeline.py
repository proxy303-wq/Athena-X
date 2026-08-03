from app.analytics.models import Analysis

from app.indicators.service import IndicatorService

from app.options.atm import ATMEngine
from app.options.greeks import GreeksEngine
from app.options.maxpain import MaxPainEngine
from app.options.oi import OIEngine
from app.options.pcr import PCREngine


class AnalyticsPipeline:

    @staticmethod
    def run(
        chain,
        candles,
    ):

        # ----------------------------------
        # Options
        # ----------------------------------

        atm = ATMEngine.calculate(chain)

        pcr = PCREngine.calculate(chain)

        oi = OIEngine.calculate(
            chain,
            atm
        )

        greeks = GreeksEngine.calculate(
            chain,
            atm
        )

        max_pain = MaxPainEngine.calculate(
            chain
        )

        # ----------------------------------
        # Technical Indicators
        # ----------------------------------

        indicators = IndicatorService(
            candles
        ).summary()

        # ----------------------------------
        # Unified Analysis
        # ----------------------------------

        return Analysis(

            atm=atm,

            pcr=pcr,

            oi=oi,

            greeks=greeks,

            max_pain=max_pain,

            indicators=indicators,

        )