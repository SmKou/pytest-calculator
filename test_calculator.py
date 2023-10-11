import pytest
from calculator import Calculator

def test_add_positive_numbers():
    calculator = Calculator()
    assert calculator.add(1, 2) == 3

def test_add_positive_and_negative():
    calculator = Calculator()
    assert calculator.add(2, -2) == 0

def test_add_negative_numbers():
    calculator = Calculator()
    assert calculator.subtract(-2, -1) == -1

def test_subtract_positive_numbers():
    calculator = Calculator()
    assert calculator.subtract(3, 1) == 2

def test_subtract_positive_and_negative():
    calculator = Calculator()
    assert calculator.subtract(2, -1) == 3

def test_subtract_negative_numbers():
    calculator = Calculator()
    assert calculator.subtract(-2, -1) == -1

def test_multiply_positive_numbers():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6

def test_multiply_positive_and_negative():
    calculator = Calculator()
    assert calculator.multiply(-2, 3) == -6

def test_multiply_negative_numbers():
    calculator = Calculator()
    assert calculator.multiply(-2, -3) == 6

def test_divide_positive_numbers():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2

def test_divide_positive_and_negative():
    calculator = Calculator()
    assert calculator.divide(6, -3) == -2

def test_divide_negative_numbers():
    calculator = Calculator()
    assert calculator.divide(-6, -2) == 3

def test_divide_raise_exception_on_zero_second_arg():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(4, 0)