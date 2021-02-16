from typing import cast

class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> None:
        # self.amount *= multiplier
        return Dollar(self._amount * multiplier)

    def equals(self, obj: object) -> bool:
        dollar = cast(Dollar, obj)
        return self._amount == dollar._amount