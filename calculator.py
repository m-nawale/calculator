"""Core arithmetic logic for the calculator application."""

from __future__ import annotations

Number = float | int


class Calculator:
    """Perform basic arithmetic operations on numeric operands."""

    @staticmethod
    def _coerce_operand(value: object, name: str) -> float:
        """Convert ``value`` to ``float`` ensuring it is numeric."""
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a real number.")
        return float(value)

    @classmethod
    def _prepare_operands(cls, a: object, b: object) -> tuple[float, float]:
        """Validate and convert operands prior to an operation."""
        return cls._coerce_operand(a, "a"), cls._coerce_operand(b, "b")

    def add(self, a: Number, b: Number) -> float:
        """Return the sum of *a* and *b*.

        Raises:
            TypeError: If either operand is not numeric.
        """
        left, right = self._prepare_operands(a, b)
        return left + right

    def subtract(self, a: Number, b: Number) -> float:
        """Return the difference of *a* and *b*.

        Raises:
            TypeError: If either operand is not numeric.
        """
        left, right = self._prepare_operands(a, b)
        return left - right

    def multiply(self, a: Number, b: Number) -> float:
        """Return the product of *a* and *b*.

        Raises:
            TypeError: If either operand is not numeric.
        """
        left, right = self._prepare_operands(a, b)
        return left * right

    def divide(self, a: Number, b: Number) -> float:
        """Return the quotient of *a* and *b*.

        Raises:
            TypeError: If either operand is not numeric.
            ValueError: If ``b`` is zero.
        """
        left, right = self._prepare_operands(a, b)
        if right == 0:
            raise ValueError("Cannot divide by zero.")
        return left / right


__all__ = ["Calculator"]
