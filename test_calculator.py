import pytest
from calculator import Calculator


class TestCalculator:

    @pytest.mark.parametrize("a,b,expected", [
        (-1, -2, -3),
        (-1, 0, -1),
        (0, 0, 0),
        (-1, 1, 0),
        (0, 1, 1),
        (1, 1, 2),
        (1, 2, 3),
        (1.5, 3.2, 4.7),
        (-1.1, 4.6, 3.5),
        (-1.1, -3.2, -4.3),
        (3.3, 3.3, 6.6),
        (3.3, 3.222, 6.522),
        (3.33333, 3.33333, 6.66666),
        (1.1111111111, 1.1111111111, 2.2222222222),
        (1.111111111111, 1.111111111111, 2.222222222222),
    ])
    def test_add(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.sum() == expected

    @pytest.mark.parametrize("a,b,expected", [
        (-1, -2, 1),
        (-1, 0, -1),
        (0, 0, 0),
        (-1, 1, -2),
        (0, 1, -1),
        (1, 1, 0),
        (1, 2, -1),
        (1.5, 3.2, -1.7),
        (-1.1, 4.6, -5.7),
        (-1.1, -3.2, 2.1),
        (3.3, 3.3, 0),
        (3.3, 3.222, 0.078),
        (3.33333, -3.33333, 6.66666),
        (1.1111111111, 2.2222222222, -1.1111111111),
        (1.111111111111, 2.222222222222, -1.111111111111),
    ])
    def test_subtract(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.subtract() == expected

    @pytest.mark.parametrize("a,b,expected", [
        (-1, -2, 2),
        (-1, 0, 0),
        (0, 0, 0),
        (-1, 1, -1),
        (0, 1, 0),
        (1, 1, 1),
        (1, 2, 2),
        (1.5, 3.2, 4.8),
        (-1.1, 4.6, -5.06),
        (0.01, 0.1, 0.001),
        (3.3, 3.3, 10.89),
        (1.1, 2.2, 2.42),
        (9.99, 3.25, 32.4675),
        (3.33333, -3.33333, -11.1110888889),
        (3.333333, -3.333333, -11.111108888889),
    ])
    def test_multiply(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.multiply() == expected

    @pytest.mark.parametrize("a,b,expected", [
        (-1, -2, 0.5),
        (2, 2, 1),
        (2, 1, 2),
    ])
    def test_divide(self, a, b, expected):
        calc = Calculator(a, b)
        assert calc.divide() == expected

    @pytest.mark.parametrize("a,b", [
        (0, 0),
        (0.0, 0),
        (0.0, 0.0),
        (0.00000, 0.000000),
        (1, 0),
        (1, 0.0),
        (2.2, 0),
        (0.000000000001, 0),
    ])
    def test_divide_by_zero(self, a, b):
        calc = Calculator(a, b)
        with pytest.raises(ZeroDivisionError) as division_error:
            calc.divide()
        assert division_error.value.args[0] == "Divisor cannot be 0"
