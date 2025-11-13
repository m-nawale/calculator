"""Command-line interface for the calculator application."""

from __future__ import annotations

from typing import Callable

import questionary

from calculator import Calculator

Operation = tuple[str, Callable[[float, float], float]]


def _prompt_number(prompt: str) -> float | None:
    """Prompt the user for a numeric value, reprompting on invalid input."""
    while True:
        response = questionary.text(prompt).ask()
        if response is None:
            return None
        try:
            return float(response)
        except (TypeError, ValueError):
            print("Please enter a valid number.")


def main() -> None:
    """Run the interactive calculator CLI."""
    calc = Calculator()

    operation = questionary.select(
        "Choose an operation:",
        choices=["Add", "Subtract", "Multiply", "Divide"],
    ).ask()

    if operation is None:
        print("No operation selected. Exiting.")
        return

    a = _prompt_number("Enter the first number:")
    if a is None:
        print("No value entered. Exiting.")
        return

    b = _prompt_number("Enter the second number:")
    if b is None:
        print("No value entered. Exiting.")
        return

    operations: dict[str, Operation] = {
        "Add": ("adding", calc.add),
        "Subtract": ("subtracting", calc.subtract),
        "Multiply": ("multiplying", calc.multiply),
        "Divide": ("dividing", calc.divide),
    }

    verb, func = operations[operation]

    try:
        result = func(a, b)
    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return

    print(f"The result of {verb} {a} and {b} is: {result}")


if __name__ == "__main__":
    main()
