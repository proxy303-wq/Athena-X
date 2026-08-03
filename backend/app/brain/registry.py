from app.brain.plugins.pcr import PCRPlugin
from app.brain.plugins.oi import OIPlugin


class BrainRegistry:

    @staticmethod
    def get():

        return [

            PCRPlugin,

            OIPlugin,

        ]