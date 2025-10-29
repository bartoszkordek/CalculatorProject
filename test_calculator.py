from calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator(1, 2)
        assert calc.sum() == 3
