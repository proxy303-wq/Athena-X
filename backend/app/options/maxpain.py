from dataclasses import dataclass

from app.options.models import OptionChain


@dataclass
class MaxPainResult:

    max_pain: float
    total_loss: float


class MaxPainEngine:

    @staticmethod
    def calculate(chain: OptionChain) -> MaxPainResult:

        strikes = chain.strikes

        lowest_loss = float("inf")
        max_pain = 0.0

        # Assume expiry at every strike
        for expiry in strikes:

            expiry_price = expiry.strike

            total_loss = 0.0

            for option in strikes:

                strike = option.strike

                # -------------------------
                # CALL LOSS
                # -------------------------

                if option.call:

                    intrinsic = max(
                        0,
                        expiry_price - strike
                    )

                    total_loss += intrinsic * option.call.open_interest

                # -------------------------
                # PUT LOSS
                # -------------------------

                if option.put:

                    intrinsic = max(
                        0,
                        strike - expiry_price
                    )

                    total_loss += intrinsic * option.put.open_interest

            if total_loss < lowest_loss:

                lowest_loss = total_loss
                max_pain = expiry_price

        return MaxPainResult(

            max_pain=max_pain,

            total_loss=lowest_loss,

        )