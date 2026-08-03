from app.brain.models import EngineScore


class PCRPlugin:

    name = "PCR"

    @staticmethod
    def score(analysis):

        pcr = analysis.pcr.pcr

        score = 0

        confidence = 50

        reasoning = []

        if pcr >= 1.5:

            score = 20
            confidence = 90
            reasoning.append(
                f"Strong Bullish PCR ({pcr})"
            )

        elif pcr >= 1.2:

            score = 15
            confidence = 80
            reasoning.append(
                f"Bullish PCR ({pcr})"
            )

        elif pcr >= 0.8:

            score = 0
            confidence = 60
            reasoning.append(
                f"Neutral PCR ({pcr})"
            )

        elif pcr >= 0.5:

            score = -15
            confidence = 80
            reasoning.append(
                f"Bearish PCR ({pcr})"
            )

        else:

            score = -20
            confidence = 90
            reasoning.append(
                f"Strong Bearish PCR ({pcr})"
            )

        return EngineScore(

            name="PCR",

            score=score,

            confidence=confidence,

            reasoning=reasoning,

        )