from app.context.service import MarketContextService

from .trend import TrendEngine
from .rsi import RSIEngine
from .structure import StructureEngine
from .vwap import VWAPEngine


class EngineRegistry:

    def __init__(self):

        self.engines = [

            TrendEngine(),
            RSIEngine(),
            StructureEngine(),
            VWAPEngine(),

        ]

    def run(self):

        context = MarketContextService.load()

        evidence = []

        for engine in self.engines:

            try:
                evidence.append(engine.analyze(context))

            except Exception as e:
                print(f"{engine.name}: {e}")

        return evidence


registry = EngineRegistry()