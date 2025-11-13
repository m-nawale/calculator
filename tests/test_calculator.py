"""Tests for the :mod:`calculator` module."""

from __future__ import annotations

import pytest

from calculator import Calculator


@pytest.fixture()
def calculator() -> Calculator:
    return Calculator()


def test_add_returns_sum(calculator: Calculator) -> None:
    assert calculator.add(2, 3) == pytest.approx(5.0)


def test_subtract_returns_difference(calculator: Calculator) -> None:
    assert calculator.subtract(5, 3) == pytest.approx(2.0)


def test_multiply_returns_product(calculator: Calculator) -> None:
    assert calculator.multiply(2, 4) == pytest.approx(8.0)


def test_divide_returns_quotient(calculator: Calculator) -> None:
    assert calculator.divide(10, 2) == pytest.approx(5.0)


def test_divide_raises_on_zero(calculator: Calculator) -> None:
    with pytest.raises(ValueError):
        calculator.divide(1, 0)


def test_operations_reject_non_numeric_input(calculator: Calculator) -> None:
    with pytest.raises(TypeError):
        calculator.add("a", 1)

    with pytest.raises(TypeError):
        calculator.multiply(1, object())


def test_operations_reject_boolean_input(calculator: Calculator) -> None:
    with pytest.raises(TypeError):
        calculator.subtract(True, 1)

    with pytest.raises(TypeError):
        calculator.divide(1, False)
