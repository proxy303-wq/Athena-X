from app.brain.models import EngineScore


class OIPlugin:

    name = "OI"

    @staticmethod
    def score(analysis):

        score = 0

        reasons = []

        if analysis.oi.support < analysis.atm.spot:

            score += 10

            reasons.append(
                "Support below spot"
            )

        if analysis.oi.resistance > analysis.atm.spot:

            score += 10

            reasons.append(
                "Resistance above spot"
            )

        return EngineScore(

            name="OI",

            score=score,

            confidence=75,

            reasoning=reasons,

        )