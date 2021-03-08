import sys
import os
from pathlib import Path
path = Path(__file__)
abs_parent_dir = os.path.join(os.path.abspath(path.parent.parent), "src")
sys.path.append(abs_parent_dir)
from money import Money
from bank import Bank
from typing import cast
from sum_val import SumVal
from expression import Expression


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

    def test_plus_resturns_sum_addend(self):
        five = Money.dollar(5)
        result = five.plus(five)
        sum_val = cast(SumVal, result)
        assert five == sum_val.addend

    def test_plus_resturns_sum_augend(self):
        five = Money.dollar(5)
        result = five.plus(five)
        sum_val = cast(SumVal, result)
        assert five == sum_val.augend

    def test_reduce_sum(self):
        sum_val = SumVal(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum_val, "USD")
        assert Money.dollar(7) == result

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        assert Money.dollar(1) == result

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        assert Money.dollar(1) == result

    def test_identity_rate(self):
        bank = Bank()
        assert 1 == bank.rate("USD", "USD")

    def test_mixed_addition(self):
        five_bucks = cast(Expression, Money.dollar(5))
        ten_francs = cast(Expression, Money.franc(10))
        bank = Bank()
        bank.add_rate("CHF", "USD", 2)
        result = bank.reduce(five_bucks.plus(ten_francs), "USD")
        assert Money.dollar(10) == result