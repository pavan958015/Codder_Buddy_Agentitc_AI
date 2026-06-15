from calculator_app.utils import math_operations
import math

class CalculatorService:
    """
    Orchestrates complex mathematical operations and manages calculator memory functions (M+, M-, MR).
    Depends on math_operations for core arithmetic logic.
    """

    def __init__(self):
        # Initialize memory state
        self._memory = 0
        print("CalculatorService initialized with memory set to 0.")

    def add(self, a: float, b: float) -> float:
        """Performs addition."""
        return math_operations.add(a, b)

    def subtract(self, a: float, b: float) -> float:
        """Performs subtraction."""
        return math_operations.subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        """Performs multiplication."""
        return math_operations.multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        """Performs division, handling division by zero."""
        return math_operations.divide(a, b)

    def power(self, base: float, exponent: float) -> float:
        """Performs power function (base ^ exponent)."""
        return math_operations.power(base, exponent)

    def square_root(self, number: float) -> float:
        """Performs square root function."""
        return math_operations.square_root(number)

    def sine(self, angle_radians: float) -> float:
        """Performs sine function."""
        return math_operations.sine(angle_radians)

    def cosine(self, angle_radians: float) -> float:
        """Performs cosine function."""
        return math_operations.cosine(angle_radians)

    def tangent(self, angle_radians: float) -> float:
        """Performs tangent function."""
        return math_operations.tangent(angle_radians)

    def logarithm(self, number: float, base: float = None) -> float:
        """Performs logarithm function."""
        if base is None:
            return math_operations.logarithm(number)
        return math_operations.logarithm(number, base)

    def clear_memory(self):
        """Clears the calculator memory."""
        self._memory = 0
        print("Calculator memory cleared.")

    def memory_plus(self, value: float):
        """Adds a value to the current memory state (M+)."""
        self._memory += value
        print(f"Memory M+ operation performed. Current memory: {self._memory}")

    def memory_minus(self, value: float):
        """Subtract a value from the current memory state (M-)."""
        self._memory -= value
        print(f"Memory M- operation performed. Current memory: {self._memory}")

    def memory_recall(self) -> float:
        """Recalls and returns the current memory value."""
        return self._memory

    def memory_recall_and_store(self, result: float):
        """Recalls the current memory value and stores it as a new value (MR)."""
        return self._memory

    def get_memory(self) -> float:
        """Returns the current memory value."""
        return self._memory

