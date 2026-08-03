from dataclasses import dataclass

from app.options.models import OptionChain


@dataclass
class ATMResult:

    spot: float

    atm_strike: float

    nearby_strikes: list[float]


class ATMEngine:

    @staticmethod
    def calculate(
        chain: OptionChain,
        range_size: int = 3
    ) -> ATMResult:

        spot = chain.spot_price

        strikes = sorted(
            [s.strike for s in chain.strikes]
        )

        # Find nearest strike
        atm = min(
            strikes,
            key=lambda x: abs(x - spot)
        )

        idx = strikes.index(atm)

        start = max(0, idx - range_size)

        end = min(
            len(strikes),
            idx + range_size + 1
        )

        nearby = strikes[start:end]

        return ATMResult(
            spot=spot,
            atm_strike=atm,
            nearby_strikes=nearby
        )