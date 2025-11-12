"""Simple demonstration script for :mod:`calculator`."""

from __future__ import annotations

from calculator import Calculator


def main() -> None:
    """Showcase the core calculator operations."""
    calculator = Calculator()

    print("Addition:", calculator.add(15, 10))
    print("Subtraction:", calculator.subtract(15, 10))
    print("Multiplication:", calculator.multiply(15, 10))

    try:
        print("Division:", calculator.divide(15, 10))
    except ValueError as error:
        print(f"Division error: {error}")


if __name__ == "__main__":
    main()
