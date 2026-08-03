from dataclasses import dataclass

from app.options.models import OptionChain
from app.options.atm import ATMResult


@dataclass
class GreeksSummary:

    strike: float

    call_delta: float
    call_gamma: float
    call_theta: float
    call_vega: float
    call_iv: float

    put_delta: float
    put_gamma: float
    put_theta: float
    put_vega: float
    put_iv: float


class GreeksEngine:

    @staticmethod
    def calculate(
        chain: OptionChain,
        atm: ATMResult
    ) -> GreeksSummary:

        atm_strike = atm.atm_strike

        for strike in chain.strikes:

            if strike.strike == atm_strike:

                return GreeksSummary(

                    strike=atm_strike,

                    call_delta=strike.call.greeks.delta,
                    call_gamma=strike.call.greeks.gamma,
                    call_theta=strike.call.greeks.theta,
                    call_vega=strike.call.greeks.vega,
                    call_iv=strike.call.greeks.iv,

                    put_delta=strike.put.greeks.delta,
                    put_gamma=strike.put.greeks.gamma,
                    put_theta=strike.put.greeks.theta,
                    put_vega=strike.put.greeks.vega,
                    put_iv=strike.put.greeks.iv,

                )

        raise Exception("ATM strike not found")