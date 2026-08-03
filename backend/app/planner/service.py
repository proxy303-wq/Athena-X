from .models import TradePlan


class TradePlanner:

    @staticmethod
    def generate(action, context):

        price = context.current_price

        if action == "BULLISH":

            entry = round(price, 2)

            sl = round(price - 35, 2)

            target1 = round(price + 45, 2)

            target2 = round(price + 90, 2)

        elif action == "BEARISH":

            entry = round(price, 2)

            sl = round(price + 35, 2)

            target1 = round(price - 45, 2)

            target2 = round(price - 90, 2)

        else:

            return None

        risk = abs(entry - sl)

        reward = abs(target2 - entry)

        rr = round(reward / risk, 2)

        return TradePlan(

            direction=action,

            entry=entry,

            stop_loss=sl,

            target1=target1,

            target2=target2,

            risk_reward=rr

        )