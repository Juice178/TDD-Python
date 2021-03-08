from __future__ import annotations
from money import Money
from expression import Expression
from dataclasses import dataclass
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from bank import Bank


@dataclass()
class SumVal(Expression):
    augend: 'Expression'
    addend: 'Expression'

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        amount = self.augend.reduce(bank, to)._amount + self.addend.reduce(bank, to)._amount
        return Money(amount, to)

    def plus(addend: Expression):
        pass
