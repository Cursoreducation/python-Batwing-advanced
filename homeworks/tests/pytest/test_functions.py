import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(5, 2) == 7
    assert Calculator.add(-40, -2 ) == -42
    assert Calculator.add(-12, 20) != 78


def test_subtract():
    assert Calculator.subtract(67, 22) == 45
    assert Calculator.subtract(23, -2) == 25
    assert Calculator.subtract(67, 9) != 21


def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 12) == -24
    assert Calculator.multiply(-121, 21) != 2


def test_divide():
    assert Calculator.divide(18, 2) == 9
    assert Calculator.divide(2, -2) == -1
    assert Calculator.divide(2121, 323) != 11
    with pytest.raises(ValueError):
        Calculator.divide(321, 0)