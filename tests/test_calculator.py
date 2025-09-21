import pytest
from app.calculator import Operations  # Import the Operations class

# ----------------- Addition Tests ----------------- #
def test_add():
    """
    Test adding two positive numbers.
    Example: 3 + 5 should return 8.
    """
    assert Operations.addition(3, 5) == 8

def test_add_negative_numbers():
    """
    Test adding negative numbers.
    Example: -2 + 3 should return 1.
             -2 + -3 should return -5.
    """
    assert Operations.addition(-2, 3) == 1
    assert Operations.addition(-2, -3) == -5    

# ----------------- Subtraction Tests ----------------- #
def test_subtract():
    """
    Test subtracting two positive numbers.
    Example: 10 - 2 should return 8.
    """
    assert Operations.subtraction(10, 2) == 8

def test_subtract_negative_numbers():
    """
    Test subtracting with negative numbers.
    Example: -5 - 3 should return -8.
             -5 - (-3) should return -2.
    """
    assert Operations.subtraction(-5, 3) == -8
    assert Operations.subtraction(-5, -3) == -2

# ----------------- Multiplication Tests ----------------- #
def test_multiply():
    """
    Test multiplying two positive numbers.
    Example: 3 * 7 should return 21.
    """
    assert Operations.multiplication(3, 7) == 21

def test_multiply_negative_numbers():
    """
    Test multiplying with negative numbers.
    Example: -3 * 7 should return -21.
             -3 * -7 should return 21.
    """
    assert Operations.multiplication(-3, 7) == -21
    assert Operations.multiplication(-3, -7) == 21

# ----------------- Division Tests ----------------- #
def test_divide():
    """
    Test dividing two positive numbers.
    Example: 4 / 2 should return 2.
    """
    assert Operations.division(4, 2) == 2

def test_divide_negative_numbers():
    """
    Test dividing with negative numbers.
    Example: -8 / 2 should return -4.
             -8 / -2 should return 4.
    """
    assert Operations.division(-8, 2) == -4
    assert Operations.division(-8, -2) == 4   

def test_divide_by_zero():
    """
    Test dividing by zero.
    This should raise a ValueError, because division by zero is not allowed.
    """
    with pytest.raises(ValueError):
        Operations.division(5, 0)
