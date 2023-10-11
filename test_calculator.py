import pytest
from calculator import Calculator

def test_add_positive_numbers():
    calculator = Calculator()
    assert calculator.add(1, 2) == 3

def test_subtract_positive_numbers():
    calculator = Calculator()
    assert calculator.subtract(3, 1) == 2

def test_multiply_positive_numbers():
    calculator = Calculator()
    assert calculator.multiply(2, 3) == 6

def test_divide_positive_numbers():
    calculator = Calculator()
    assert calculator.divide(6, 3) == 2