from pydantic import BaseModel

from app.options.atm import ATMResult
from app.options.greeks import GreeksSummary
from app.options.maxpain import MaxPainResult
from app.options.oi import OIResult
from app.options.pcr import PCRResult

from app.indicators.service import IndicatorSummary


class Analysis(BaseModel):

    # ------------------------
    # Options
    # ------------------------

    atm: ATMResult

    pcr: PCRResult

    oi: OIResult

    max_pain: MaxPainResult

    greeks: GreeksSummary

    # ------------------------
    # Technical Indicators
    # ------------------------

    indicators: IndicatorSummary