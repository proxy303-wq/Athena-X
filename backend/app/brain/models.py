from pydantic import BaseModel


class EngineScore(BaseModel):

    name: str

    score: float

    confidence: float

    reasoning: list[str]


class BrainResult(BaseModel):

    total_score: float

    confidence: float

    action: str

    engines: list[EngineScore]

    reasoning: list[str]