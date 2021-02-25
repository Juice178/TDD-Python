from __future__ import annotations
from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from dollar import Dollar
from abc import ABC, abstractstaticmethod


class Money(ABC):
    def __init__(self, amount: int) -> None:
        self._amount = amount

    def equals(self, obj: object) -> bool:
        money = cast(Money, obj)
        print(type(self), type(obj))
        return self._amount == money._amount and type(self) == type(obj)

    @staticmethod
    def dollar(amount: int) -> Money:
        from dollar import Dollar
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> Money:
        from franc import Franc
        return Franc(amount)
    
    @abstractstaticmethod
    def times(self, multiplier: int) -> Money:
        pass