from __future__ import annotations
from typing import cast, TYPE_CHECKING
if TYPE_CHECKING:
    from dollar import Dollar
from expression import Expression
# from abc import ABC, abstractmethod
from dataclasses import dataclass, field
if TYPE_CHECKING:
    from bank import Bank


@dataclass()
class Money(Expression):
    _amount: int = field(default_factory=int)
    _currency: str = field(default_factory=str)
    # def __init__(self, amount: int, currency: str) -> None:
    #     self._amount = amount
    #     self._currency = currency

    # @abstractmethod
    def times(self, multiplier: int) -> Money:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend) -> Expression:
        from sum_val import SumVal
        return SumVal(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> Money:
        # rate = 2 if self._currency == "CHF" and to == "USD" else 1
        rate = bank.rate(self._currency, to)
        return Money(self._amount / rate, to)

    def get_currency(self) -> str:
        return self._currency

    def equals(self, obj: object) -> bool:
        money = cast(Money, obj)
        return self._amount == money._amount and self.get_currency() == money.get_currency()

    def __str__(self) -> str:
        return f"{self._amount} {self._currency}"

    @staticmethod
    def dollar(amount: int) -> Money:
        # from dollar import Dollar
        return Money(amount, "USD")

    @staticmethod
    def franc(amount: int) -> Money:
        # from franc import Franc
        return Money(amount, "CHF")

    
