"""
A simple calculator library for basic arithmetic operations.
This is a demo project for practicing open source licensing.
"""

class SimpleCalculator:
    """A simple calculator class."""

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference of a and b (a - b)."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Return the quotient of a and b (a / b).
        Raises ValueError if b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b


# Example usage
if __name__ == "__main__":
    calc = SimpleCalculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
    print(f"5 * 3 = {calc.multiply(5, 3)}")
    print(f"5 / 3 = {calc.divide(5, 3):.2f}")