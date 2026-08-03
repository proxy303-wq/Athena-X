from app.options.models import OptionChain

from app.optionchain.models import (
    OptionChainResponse,
    OptionChainRow,
)


class OptionChainService:

    @staticmethod
    def build(chain: OptionChain) -> OptionChainResponse:

        # -------------------------
        # Find ATM Strike
        # -------------------------

        atm = min(
            chain.strikes,
            key=lambda s: abs(s.strike - chain.spot_price),
        ).strike

        rows = []

        # -------------------------
        # Build Rows
        # -------------------------

        for strike in chain.strikes:

            rows.append(

                OptionChainRow(

                    strike=strike.strike,

                    # -------------------
                    # CALL
                    # -------------------

                    call_ltp=(
                        strike.call.ltp
                        if strike.call
                        else None
                    ),

                    call_oi=(
                        strike.call.open_interest
                        if strike.call
                        else None
                    ),

                    call_volume=(
                        strike.call.volume
                        if strike.call
                        else None
                    ),

                    call_iv=(
                        strike.call.greeks.iv
                        if strike.call
                        else None
                    ),

                    call_delta=(
                        strike.call.greeks.delta
                        if strike.call
                        else None
                    ),

                    # -------------------
                    # PUT
                    # -------------------

                    put_ltp=(
                        strike.put.ltp
                        if strike.put
                        else None
                    ),

                    put_oi=(
                        strike.put.open_interest
                        if strike.put
                        else None
                    ),

                    put_volume=(
                        strike.put.volume
                        if strike.put
                        else None
                    ),

                    put_iv=(
                        strike.put.greeks.iv
                        if strike.put
                        else None
                    ),

                    put_delta=(
                        strike.put.greeks.delta
                        if strike.put
                        else None
                    ),

                    # -------------------
                    # ATM
                    # -------------------

                    is_atm=(strike.strike == atm),

                )

            )

        return OptionChainResponse(

            spot=chain.spot_price,

            expiry=chain.expiry,

            rows=rows,

        )