from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from money import Money

class Expression(ABC):
    @abstractmethod
    def reduce(self, to: str) -> "Money":
        pass
