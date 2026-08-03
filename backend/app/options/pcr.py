from dataclasses import dataclass

from app.options.models import OptionChain


@dataclass
class PCRResult:

    total_call_oi: int

    total_put_oi: int

    pcr: float

    sentiment: str


class PCREngine:

    @staticmethod
    def calculate(chain: OptionChain) -> PCRResult:

        total_call = 0

        total_put = 0

        for strike in chain.strikes:

            if strike.call:

                total_call += strike.call.open_interest

            if strike.put:

                total_put += strike.put.open_interest

        if total_call == 0:

            pcr = 0

        else:

            pcr = total_put / total_call

        # --------------------
        # Sentiment
        # --------------------

        if pcr < 0.8:

            sentiment = "BEARISH"

        elif pcr < 1.2:

            sentiment = "NEUTRAL"

        else:

            sentiment = "BULLISH"

        return PCRResult(

            total_call_oi=total_call,

            total_put_oi=total_put,

            pcr=round(pcr, 2),

            sentiment=sentiment,

        )