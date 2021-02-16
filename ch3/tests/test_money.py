import sys
import os
from pathlib import Path
path = Path(__file__)
abs_parent_dir = os.path.join(os.path.abspath(path.parent.parent), "src")
sys.path.append(abs_parent_dir)
from dollar import Dollar


class TestMoney:
    def test_multiplication_one(self):
        five = Dollar(5)
        product = five.times(2)
        assert 10 == product.amount
    
    def test_multiplication_two(self):
        five = Dollar(5)
        product = five.times(3)
        assert 15 == product.amount

    def test_equality_one(self):
        assert Dollar(5).equals(Dollar(5))

    def test_equality_two(self):
        assert not Dollar(5).equals(Dollar(6))