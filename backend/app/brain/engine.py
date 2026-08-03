from app.brain.models import BrainResult
from app.brain.registry import BrainRegistry
from app.brain.weights import ENGINE_WEIGHTS


class AthenaBrain:

    @staticmethod
    def think(analysis):

        total_score = 0.0
        total_possible = 0.0

        engine_results = []
        reasoning = []

        for engine in BrainRegistry.get():

            result = engine.score(analysis)

            # Weight for this engine
            weight = ENGINE_WEIGHTS.get(
                result.name.upper(),
                10
            )

            # Plugin returns score between -1 and +1
            weighted_score = result.score * weight

            total_score += weighted_score
            total_possible += weight

            engine_results.append(result)
            reasoning.extend(result.reasoning)

        # ----------------------------
        # Confidence
        # ----------------------------

        if total_possible == 0:
            confidence = 0
        else:
            confidence = round(
                abs(total_score) / total_possible * 100,
                2
            )

        # ----------------------------
        # Final Action
        # ----------------------------

        if total_score >= 0.70 * total_possible:

            action = "STRONG BUY"

        elif total_score >= 0.30 * total_possible:

            action = "BUY"

        elif total_score <= -0.70 * total_possible:

            action = "STRONG SELL"

        elif total_score <= -0.30 * total_possible:

            action = "SELL"

        else:

            action = "WAIT"

        return BrainResult(

            total_score=round(total_score, 2),

            confidence=confidence,

            action=action,

            engines=engine_results,

            reasoning=reasoning,

        )