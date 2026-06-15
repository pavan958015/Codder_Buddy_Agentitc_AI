import unittest
import math
from calculator_app.utils.math_operations import (
    add, subtract, multiply, divide, power, square_root, 
    sine, cosine, tangent, logarithm
)

class TestMathOperations(unittest.TestCase):

    # --- Tests for basic arithmetic operations ---

    def test_add(self):
        """Test the addition function."""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 10), 9)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the subtraction function."""
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(5, 8), -3)
        self.assertEqual(subtract(-5, -2), -3)

    def test_multiply(self):
        """Test the multiplication function."""
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(multiply(-2, 6), -12)
        self.assertEqual(multiply(0, 99), 0)

    def test_divide(self):
        """Test the division function."""
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 3), 7/3)
        # Test division by zero error handling
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            divide(10, 0)

    def test_power(self):
        """Test the power function."""
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertAlmostEqual(power(4, 0.5), 2.0) # Square root check

    # --- Tests for mathematical functions using math module ---

    def test_square_root(self):
        """Test the square root function."""
        self.assertEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(1), 1.0)
        # Test error handling for negative numbers
        with self.assertRaisesRegex(ValueError, "Cannot calculate the square root of a negative number"):
            square_root(-4)

    def test_sine_cosine_tangent(self):
        """Test trigonometric functions with known values (using radians)."""
        # Test sine: sin(pi/2) should be 1.0
        self.assertAlmostEqual(sine(math.pi / 2), 1.0)
        # Test cosine: cos(0) should be 1.0
        self.assertAlmostEqual(cosine(0), 1.0)
        # Test tangent: tan(pi/4) should be 1.0
        self.assertAlmostEqual(tangent(math.pi / 4), 1.0)

    def test_logarithm(self):
        """Test the logarithm function."""
        # Natural logarithm (base e) of e should be 1
        self.assertAlmostEqual(logarithm(math.e, math.e), 1.0)
        # Log base 10 of 10 should be 1
        self.assertAlmostEqual(logarithm(10, 10), 1.0)
        # Logarithm of 1 should be 0
        self.assertAlmostEqual(logarithm(1, math.e), 0.0)
        # Test error handling for non-positive numbers
        with self.assertRaisesRegex(ValueError, "Logarithm argument must be positive"):
            logarithm(0)
        with self.assertRaisesRegex(ValueError, "Logarithm argument must be positive"):
            logarithm(-5)

if __name__ == '__main__':
    unittest.main()