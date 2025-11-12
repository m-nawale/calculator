# ================================
# Calculator Class
# ================================

class Calculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("Addition: ", calc.add(10, 5))
    print("Subtraction: ", calc.subtract(10, 5))
    print("Multiplication: ", calc.multiply(10, 5))
    print("Division: ", calc.divide(10, 5))
    