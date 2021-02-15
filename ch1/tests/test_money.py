import sys
import os
from pathlib import Path
path = Path(__file__)
abs_parent_dir = os.path.join(os.path.abspath(path.parent.parent), "src")
sys.path.append(abs_parent_dir)
from dollar import Dollar


class TestMoney:
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)
        assert 10 == five.amount