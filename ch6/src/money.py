from typing import cast

class Money:
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, obj: object) -> bool:
        money = cast(Money, obj)
        return self._amount == money._amount