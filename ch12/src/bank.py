from money import Money
from expression import Expression
from typing import cast
from sum_val import SumVal


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        # if isinstance(source, Money):
        #     return source.reduce(to)
        # sum_val = cast(SumVal, source)
        # # amount = sum_val.augend._amount + sum_val.addend._amount
        # # return Money(amount, to)
        return source.reduce(to)