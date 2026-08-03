from abc import ABC, abstractmethod

from app.core.models import Evidence


class BaseEngine(ABC):

    name: str = "Base Engine"

    @abstractmethod
    def analyze(self) -> Evidence:
        """
        Every engine must return one Evidence object.
        """
        pass