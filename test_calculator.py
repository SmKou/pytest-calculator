import pytest
from calculator import Calculator

def test_calculator_add():
    input = {
        3: [1, 2],
        0: [2, -2],
        -1: [-3, 2],
        -3: [-1, -2]
    }
    calculator = Calculator()
    for k in input:
        a = input[k][0]
        b = input[k][1]
        assert calculator.add(a, b) == k

def test_calculator_subtract():
    input = {
        2: [3, 1],
        -2: [1, 3],
        3: [2, -1],
        -3: [-1, 2],
        -1: [-2, -1],
        1: [-1, -2]
    }
    calculator = Calculator()
    for k in input:
        a = input[k][0]
        b = input[k][1]
        assert calculator.subtract(a, b) == k

def test_calculator_multiply():
    input = {
        6: [2, 3],
        -6: [-2, 3],
        -4: [2, -2],
        4: [-2, -2]
    }
    calculator = Calculator()
    for k in input:
        a = input[k][0]
        b = input[k][1]
        assert calculator.multiply(a, b) == k

def test_calculator_divide():
    input = {
        2: [6, 3],
        0.5: [3, 6],
        -4: [8, -2],
        -2: [-6, 3],
        3: [-6, -2],
        0.25: [-1, -4]
    }
    calculator = Calculator()
    for k in input:
        a = input[k][0]
        b = input[k][1]
        assert calculator.divide(a, b) == k

def test_divide_raise_exception_on_zero_second_arg():
    calculator = Calculator()
    with pytest.raises(ValueError):
        calculator.divide(4, 0)