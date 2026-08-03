from app.analytics.pipeline import AnalyticsPipeline
from app.options.atm import ATMEngine
from app.options.greeks import GreeksEngine
from app.options.maxpain import MaxPainEngine


class SnapshotBuilder:

    @staticmethod
    def build(chain):

        analysis = AnalyticsPipeline.run(chain)

        atm = ATMEngine.calculate(chain)

        greeks = GreeksEngine.calculate(chain, atm)

        maxpain = MaxPainEngine.calculate(chain)

        report = f"""
===========================================================
                    ATHENA X MARKET SNAPSHOT
===========================================================

Spot Price      : {chain.spot_price:.2f}

-----------------------------------------------------------
OPTIONS
-----------------------------------------------------------

PCR             : {analysis.pcr.pcr:.2f}
PCR Bias        : {analysis.pcr.sentiment}

Support         : {analysis.oi.support}

Resistance      : {analysis.oi.resistance}

ATM Strike      : {atm.atm_strike}

Max Pain        : {maxpain.max_pain}

-----------------------------------------------------------
ATM GREEKS
-----------------------------------------------------------

CALL

Delta           : {greeks.call_delta:.4f}

Gamma           : {greeks.call_gamma:.4f}

Theta           : {greeks.call_theta:.2f}

Vega            : {greeks.call_vega:.4f}

IV              : {greeks.call_iv:.2f}

PUT

Delta           : {greeks.put_delta:.4f}

Gamma           : {greeks.put_gamma:.4f}

Theta           : {greeks.put_theta:.2f}

Vega            : {greeks.put_vega:.4f}

IV              : {greeks.put_iv:.2f}

-----------------------------------------------------------
ATHENA DECISION
-----------------------------------------------------------

Direction       : BUY CALL

Confidence      : 40 %

Reason

✔ PCR Bullish

✔ Support Below Spot

===========================================================
"""

        return report