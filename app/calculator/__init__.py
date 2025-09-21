# This 4 methods are inside this file addition, subtraction, multiplication, and division.
# These methods are encapsulated within the `Operations` class, providing a structured way to perform basic math on two numbers.

class Operations:
    """
    The Operations class serves as a container for basic math operations.
    By using static methods, we can perform these operations without needing to create an instance of the class.
    """

    @staticmethod
    def addition(a: float, b: float) -> float:
        """
        Takes two numbers and returns their sum.
        Example: Operations.addition(5, 3) -> 8
        """
        return a + b

    @staticmethod
    def subtraction(a: float, b: float) -> float:
        """
        Takes two numbers and returns their difference.
        Example: Operations.subtraction(10, 4) -> 6
        """
        return a - b

    @staticmethod
    def multiplication(a: float, b: float) -> float:
        """
        Takes two numbers and returns their product.
        Example: Operations.multiplication(2, 3) -> 6
        """
        return a * b

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Takes two numbers and returns their quotient.
        Raises ValueError if the second number is zero.
        Example: Operations.division(10, 2) -> 5
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
