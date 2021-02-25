from __future__ import annotations
from typing import cast
from money import Money


class Dollar(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount)

    def times(self, multiplier: int) -> Money:
        # self.amount *= multiplier
        return Dollar(self._amount * multiplier)