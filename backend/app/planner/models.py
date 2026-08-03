from pydantic import BaseModel


class TradePlan(BaseModel):

    direction: str

    entry: float

    stop_loss: float

    target1: float

    target2: float

    risk_reward: float