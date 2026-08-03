from app.analytics.models import Analysis
from app.decision.models import TradePlan


class DecisionEngine:

    @staticmethod
    def calculate(analysis: Analysis):

        score = 0
        reasons = []

        # =====================================================
        # TREND
        # =====================================================

        trend = "SIDEWAYS"

        if analysis.indicators.price_above_ema20:
            score += 10
            reasons.append("Price above EMA20")
        else:
            score -= 10
            reasons.append("Price below EMA20")

        if analysis.indicators.ema20_above_ema50:
            score += 10
            reasons.append("EMA20 above EMA50")
            trend = "BULLISH"
        else:
            score -= 10
            reasons.append("EMA20 below EMA50")
            trend = "BEARISH"

        if analysis.indicators.price_above_vwap:
            score += 10
            reasons.append("Price above VWAP")
        else:
            score -= 10
            reasons.append("Price below VWAP")

        # =====================================================
        # RSI
        # =====================================================

        rsi = analysis.indicators.rsi

        if 50 <= rsi <= 70:
            score += 5
            reasons.append(f"Healthy RSI ({rsi:.1f})")

        elif rsi > 75:
            score -= 5
            reasons.append(f"RSI Overbought ({rsi:.1f})")

        elif rsi < 30:
            score += 5
            reasons.append(f"RSI Oversold ({rsi:.1f})")

        # =====================================================
        # PCR
        # =====================================================

        if analysis.pcr.pcr >= 1.5:
            score += 20
            reasons.append(f"Strong Bullish PCR ({analysis.pcr.pcr:.2f})")

        elif analysis.pcr.pcr >= 1.2:
            score += 15
            reasons.append(f"Bullish PCR ({analysis.pcr.pcr:.2f})")

        elif analysis.pcr.pcr <= 0.5:
            score -= 20
            reasons.append(f"Strong Bearish PCR ({analysis.pcr.pcr:.2f})")

        elif analysis.pcr.pcr <= 0.8:
            score -= 15
            reasons.append(f"Bearish PCR ({analysis.pcr.pcr:.2f})")

        # =====================================================
        # OI
        # =====================================================

        if analysis.oi.support < analysis.atm.spot:
            score += 5
            reasons.append(f"Support at {analysis.oi.support}")

        if analysis.oi.resistance > analysis.atm.spot:
            score += 5
            reasons.append(f"Resistance at {analysis.oi.resistance}")

        # =====================================================
        # MAX PAIN
        # =====================================================

        if analysis.atm.spot > analysis.max_pain.max_pain:
            score += 5
            reasons.append("Spot above Max Pain")
        else:
            score -= 5
            reasons.append("Spot below Max Pain")

        # =====================================================
        # GREEKS
        # =====================================================

        if analysis.greeks.call_delta > 0.50:
            score += 5
            reasons.append("Bullish Call Delta")

        if analysis.greeks.put_delta < -0.50:
            score -= 5
            reasons.append("Strong Put Delta")

        # =====================================================
        # DECISION
        # =====================================================

        if score >= 50:
            direction = "STRONG BUY CALL"

        elif score >= 25:
            direction = "BUY CALL"

        elif score <= -50:
            direction = "STRONG BUY PUT"

        elif score <= -25:
            direction = "BUY PUT"

        else:
            direction = "WAIT"

        confidence = min(
            round(abs(score) / 70 * 100),
            100,
        )

        # =====================================================
        # TRADE LEVELS
        # =====================================================

        entry = analysis.atm.spot

        if "CALL" in direction:

            stop_loss = entry - 40

            target1 = entry + 60

            target2 = entry + 120

        elif "PUT" in direction:

            stop_loss = entry + 40

            target1 = entry - 60

            target2 = entry - 120

        else:

            stop_loss = entry

            target1 = entry

            target2 = entry

        # =====================================================
        # SETUP
        # =====================================================

        if trend == "BULLISH":

            setup = "Trend Continuation"

        elif trend == "BEARISH":

            setup = "Downtrend"

        else:

            setup = "Range"

        # =====================================================
        # RISK
        # =====================================================

        if confidence >= 80:

            risk = "LOW"

        elif confidence >= 60:

            risk = "MEDIUM"

        else:

            risk = "HIGH"

        # =====================================================
        # RETURN
        # =====================================================

        return TradePlan(

            direction=direction,

            confidence=confidence,

            trend=trend,

            setup=setup,

            risk=risk,

            entry=entry,

            stop_loss=stop_loss,

            target1=target1,

            target2=target2,

            reasoning=reasons,

        )