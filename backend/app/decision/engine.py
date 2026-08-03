from app.core.models import Evidence, Signal
from .models import Decision


def evaluate(evidence_list: list[Evidence]) -> Decision:

    bullish = 0.0
    bearish = 0.0
    neutral = 0.0

    reasons = []

    for item in evidence_list:

        weighted_score = item.confidence * item.weight

        reasons.extend(item.reasons)

        if item.signal == Signal.BULLISH:
            bullish += weighted_score

        elif item.signal == Signal.BEARISH:
            bearish += weighted_score

        else:
            neutral += weighted_score

    total = bullish + bearish + neutral

    if total == 0:
        return Decision(
            action=Signal.NEUTRAL,
            confidence=0,
            score=0,
            evidence=[]
        )

    confidence = max(bullish, bearish, neutral) / total

    if bullish > bearish and bullish > neutral:

        signal = Signal.BULLISH

    elif bearish > bullish and bearish > neutral:

        signal = Signal.BEARISH

    else:

        signal = Signal.NEUTRAL

    return Decision(
        action=signal,
        confidence=round(confidence * 100, 2),
        score=round(total, 2),
        evidence=reasons
    )