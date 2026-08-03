from dataclasses import dataclass

from app.options.models import OptionChain
from app.options.atm import ATMResult


@dataclass
class OILevel:
    strike: float

    call_oi: int
    put_oi: int

    call_volume: int
    put_volume: int


@dataclass
class OIResult:
    support: float
    resistance: float

    strongest_call: OILevel
    strongest_put: OILevel

    top_call_writers: list[OILevel]
    top_put_writers: list[OILevel]


class OIEngine:

    @staticmethod
    def calculate(
        chain: OptionChain,
        atm: ATMResult,
    ) -> OIResult:

        levels = []

        # ----------------------------------
        # Build OI Levels around ATM
        # ----------------------------------

        nearby = set(atm.nearby_strikes)

        for strike in chain.strikes:

            if strike.strike not in nearby:
                continue

            level = OILevel(

                strike=strike.strike,

                call_oi=strike.call.open_interest if strike.call else 0,
                put_oi=strike.put.open_interest if strike.put else 0,

                call_volume=strike.call.volume if strike.call else 0,
                put_volume=strike.put.volume if strike.put else 0,

            )

            levels.append(level)

        if not levels:
            raise Exception("No nearby option strikes found.")

        # ----------------------------------
        # Support = Highest PUT OI
        # below/current spot
        # ----------------------------------

        below_spot = [
            x for x in levels
            if x.strike <= atm.spot
        ]

        if below_spot:
            strongest_put = max(
                below_spot,
                key=lambda x: x.put_oi
            )
        else:
            strongest_put = max(
                levels,
                key=lambda x: x.put_oi
            )

        # ----------------------------------
        # Resistance = Highest CALL OI
        # above/current spot
        # ----------------------------------

        above_spot = [
            x for x in levels
            if x.strike >= atm.spot
        ]

        if above_spot:
            strongest_call = max(
                above_spot,
                key=lambda x: x.call_oi
            )
        else:
            strongest_call = max(
                levels,
                key=lambda x: x.call_oi
            )

        # ----------------------------------
        # Top Call Writers
        # ----------------------------------

        top_call = sorted(
            levels,
            key=lambda x: x.call_oi,
            reverse=True
        )[:3]

        # ----------------------------------
        # Top Put Writers
        # ----------------------------------

        top_put = sorted(
            levels,
            key=lambda x: x.put_oi,
            reverse=True
        )[:3]

        return OIResult(

            support=strongest_put.strike,

            resistance=strongest_call.strike,

            strongest_call=strongest_call,

            strongest_put=strongest_put,

            top_call_writers=top_call,

            top_put_writers=top_put,

        )