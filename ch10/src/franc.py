from typing import cast, ClassVar
from money import Money
from dataclasses import dataclass, field


@dataclass()
class Franc(Money):
    # currency: str = field(default_factory=str, init=False)
    # currency: ClassVar[str] = "CHF"

    def __init__(self, amount: int, currency: str) -> None:
        super().__init__(amount, currency)
        # self.currency = currency

    # def times(self, multiplier: int) -> Money:
    #     # self.amount *= multiplier
    #     return Money(self._amount * multiplier, self._currency)