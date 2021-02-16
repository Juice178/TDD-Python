from typing import cast

class Dollar:
    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, multiplier: int) -> None:
        # self.amount *= multiplier
        return Dollar(self.amount * multiplier)

    def equals(self, obj: object) -> bool:
        dollar = cast(Dollar, obj)
        return self.amount == dollar.amount