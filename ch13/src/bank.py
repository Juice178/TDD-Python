from money import Money
from expression import Expression
from typing import cast
from sum_val import SumVal
from dataclasses import dataclass, field
from typing import Dict
from pair import Pair


@dataclass()
class Bank:
    _rates: Dict[Pair, int] = field(init=False)

    def __post_init__(self):
        self._rates = {}

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, source: str, to:str, rate:int) -> None:
        # print("self._rates", self._rates)
        self._rates[Pair(source, to)] = rate

    def rate(self, source: str, to:str) -> int:
        if source == to:
            return 1
        return self._rates[Pair(source, to)]