from functions_to_tests import Calculator


def test_add():
    assert Calculator.add(3,3) == 6
    assert Calculator.add(0, 3) == 3
    assert Calculator.add(-1, 3) == 2
    assert Calculator.add(-2, -1) == -3

def test_subtract():
    assert Calculator.subtract(3,3) == 0
    assert Calculator.subtract(0, 3) == -3
    assert Calculator.subtract(-1, 3) == -4
    assert Calculator.subtract(-2, -1) == -1

def test_multiply():
    assert Calculator.multiply(3,3) == 9
    assert Calculator.multiply(0, 3) == 0
    assert Calculator.multiply(-1, 3) == -3
    assert Calculator.multiply(-2, -1) == 2

def test_divide():
    assert Calculator.divide(3,3) == 1
    assert Calculator.divide(0, 3) == 0
    assert Calculator.divide(-1, 2) == -0.5
    assert Calculator.divide(-2, -1) == 2

