import unittest
from calculator_app.services.calculator_service import CalculatorService

class TestCalculatorService(unittest.TestCase):

    def setUp(self):
        """Set up a fresh instance of the service before each test."""
        self.service = CalculatorService()

    def test_initialization(self):
        """Test if the service initializes correctly."""
        self.assertIsInstance(self.service, CalculatorService)
        self.assertEqual(self.service.get_memory(), 0)

    def test_add_operation(self):
        """Test basic addition logic."""
        result = self.service.add(5, 3)
        self.assertEqual(result, 8)

    def test_subtract_operation(self):
        """Test basic subtraction logic."""
        result = self.service.subtract(15, 7)
        self.assertEqual(result, 8)

    def test_multiply_operation(self):
        """Test basic multiplication logic."""
        result = self.service.multiply(4, 5)
        self.assertEqual(result, 20)

    def test_divide_operation(self):
        """Test basic division logic."""
        result = self.service.divide(10, 2)
        self.assertEqual(result, 5.0)

    def test_power_operation(self):
        """Test power function."""
        result = self.service.power(2, 3)
        self.assertEqual(result, 8.0)

    def test_square_root_operation(self):
        """Test square root function."""
        result = self.service.square_root(9)
        self.assertEqual(result, 3.0)

    def test_memory_plus_m_plus(self):
        """Test Memory Plus (M+). Should add the current value to memory."""
        self.service.memory_plus(5)
        self.assertEqual(self.service.get_memory(), 5)
        self.service.memory_plus(10)
        self.assertEqual(self.service.get_memory(), 15)

    def test_memory_minus_m_minus(self):
        """Test Memory Minus (M-). Should subtract the current value from memory."""
        self.service.memory_plus(20)
        self.service.memory_minus(5)
        self.assertEqual(self.service.get_memory(), 15)

    def test_memory_recall_mr(self):
        """Test Memory Recall (MR). Should retrieve the stored value."""
        self.service.memory_plus(99)
        result = self.service.memory_recall()
        self.assertEqual(result, 99)

    def test_clear_memory(self):
        """Test clearing memory."""
        self.service.memory_plus(10)
        self.service.clear_memory()
        self.assertEqual(self.service.get_memory(), 0)

if __name__ == '__main__':
    unittest.main()