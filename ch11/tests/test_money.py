import sys
import os
from pathlib import Path
path = Path(__file__)
abs_parent_dir = os.path.join(os.path.abspath(path.parent.parent), "src")
sys.path.append(abs_parent_dir)
# from dollar import Dollar
# from franc import Franc
from money import Money
from bank import Bank
from typing import cast


class TestMoney:
    def test_multiplication_one(self):
        five: Money = cast(Money, Money.dollar(5))
        # product = five.times(2)
        assert Money.dollar(10).equals(five.times(2))
    
    def test_multiplication_two(self):
        five: Money = cast(Money, Money.dollar(5))
        # product = five.times(3)
        assert Money.dollar(15).equals(five.times(3))

    def test_equality_one(self):
        assert Money.dollar(5).equals(Money.dollar(5))

    def test_equality_two(self):
        assert not Money.dollar(5).equals(Money.dollar(6))

    def test_franc_dollar_equality(self):
        assert not Money.franc(5).equals(Money.dollar(5))

    def test_currency_usd(self):
        assert "USD" == Money.dollar(1).get_currency()

    def test_currency_chf(self):
        assert "CHF" == Money.franc(1).get_currency()

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum_val = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum_val, "USD")
        assert Money.dollar(10) == reduced
