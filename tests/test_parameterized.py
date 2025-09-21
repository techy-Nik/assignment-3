"""
tests/test_operations.py alias name

This module contains unit tests for the Operations class.
We use parameterized tests with pytest to efficiently test multiple
input scenarios for addition, subtraction, multiplication, and division.
"""

import pytest
from app.calculator import Operations
from typing import Union

# Define a type alias for numbers
Number = Union[int, float]

# ------------------ Addition Tests ------------------ #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 3.5, 6.0),
        (-2.5, 3.5, 1.0),
    ]
)
def test_addition(a: Number, b: Number, expected: Number) -> None:
    """Test addition with multiple combinations of integers and floats."""
    result = Operations.addition(a, b)
    assert result == expected, f"Expected {a} + {b} = {expected}, got {result}"

# ------------------ Subtraction Tests ------------------ #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (-5, -3, -2),
        (10.5, 5.5, 5.0),
        (-10.5, -5.5, -5.0),
        (0, 0, 0),
    ]
)
def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    """Test subtraction with various integers and floats."""
    result = Operations.subtraction(a, b)
    assert result == expected, f"Expected {a} - {b} = {expected}, got {result}"

# ------------------ Multiplication Tests ------------------ #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (-2, -3, 6),
        (2.5, 4.0, 10.0),
        (-2.5, 4.0, -10.0),
        (0, 5, 0),
    ]
)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    """Test multiplication with integers, negative numbers, and floats."""
    result = Operations.multiplication(a, b)
    assert result == expected, f"Expected {a} * {b} = {expected}, got {result}"

# ------------------ Division Tests ------------------ #
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),
        (-6, -3, 2.0),
        (6.0, 3.0, 2.0),
        (-6.0, 3.0, -2.0),
        (0, 5, 0.0),
    ]
)
def test_division(a: Number, b: Number, expected: float) -> None:
    """Test division with integers, negative numbers, and floats."""
    result = Operations.division(a, b)
    assert result == expected, f"Expected {a} / {b} = {expected}, got {result}"

# ------------------ Division by Zero Tests ------------------ #
@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (-1, 0),
        (0, 0),
    ]
)
def test_division_by_zero(a: Number, b: Number) -> None:
    """Test that dividing by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        Operations.division(a, b)
