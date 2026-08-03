from app.options.models import (
    Greeks,
    Option,
    Strike,
    OptionChain,
)


class OptionParser:

    @staticmethod
    def parse(raw: dict, underlying: str, expiry: str) -> OptionChain:

        strikes = []

        for strike_price, data in raw["strikes"].items():

            call = None
            put = None

            # -------------------------
            # CALL
            # -------------------------

            if "CE" in data:

                ce = data["CE"]

                call = Option(

                    strike=float(strike_price),

                    option_type="CE",

                    trading_symbol=ce["trading_symbol"],

                    ltp=float(ce["ltp"]),

                    open_interest=int(ce["open_interest"]),

                    volume=int(ce["volume"]),

                    greeks=Greeks(
                        delta=float(ce["greeks"]["delta"]),
                        gamma=float(ce["greeks"]["gamma"]),
                        theta=float(ce["greeks"]["theta"]),
                        vega=float(ce["greeks"]["vega"]),
                        rho=float(ce["greeks"]["rho"]),
                        iv=float(ce["greeks"]["iv"]),
                    ),
                )

            # -------------------------
            # PUT
            # -------------------------

            if "PE" in data:

                pe = data["PE"]

                put = Option(

                    strike=float(strike_price),

                    option_type="PE",

                    trading_symbol=pe["trading_symbol"],

                    ltp=float(pe["ltp"]),

                    open_interest=int(pe["open_interest"]),

                    volume=int(pe["volume"]),

                    greeks=Greeks(
                        delta=float(pe["greeks"]["delta"]),
                        gamma=float(pe["greeks"]["gamma"]),
                        theta=float(pe["greeks"]["theta"]),
                        vega=float(pe["greeks"]["vega"]),
                        rho=float(pe["greeks"]["rho"]),
                        iv=float(pe["greeks"]["iv"]),
                    ),
                )

            strikes.append(

                Strike(

                    strike=float(strike_price),

                    call=call,

                    put=put,

                )

            )

        return OptionChain(

            underlying=underlying,

            expiry=expiry,

            spot_price=float(raw["underlying_ltp"]),

            strikes=strikes,

        )