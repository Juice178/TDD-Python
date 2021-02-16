from typing import cast

class Franc:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def times(self, multiplier: int) -> None:
        # self.amount *= multiplier
        return Franc(self._amount * multiplier)

    def equals(self, obj: object) -> bool:
        franc = cast(Franc, obj)
        return self._amount == franc._amount