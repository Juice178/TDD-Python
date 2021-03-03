from __future__ import annotations
from money import Money
from expression import Expression
from dataclasses import dataclass


@dataclass()
class SumVal(Expression):
    augend: 'Money'
    addend: 'Money'

    def reduce(self, to: str) -> 'Money':
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)
