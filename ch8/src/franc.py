from typing import cast
from money import Money


class Franc(Money):
    def __init__(self, amount: int) -> None:
        super().__init__(amount)

    def times(self, multiplier: int) -> Money:
        # self.amount *= multiplier
        return Franc(self._amount * multiplier)