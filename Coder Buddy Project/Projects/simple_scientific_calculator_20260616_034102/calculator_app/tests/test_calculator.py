import unittest
from fastapi.testclient import TestClient
from calculator_app.main import app

class TestCalculatorAPI(unittest.TestCase):

    def setUp(self):
        """Set up the FastAPI TestClient before each test."""
        self.client = TestClient(app)

    def test_root_endpoint(self):
        """Test the root index route serves successfully."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_successful_addition(self):
        """Test POST /api/calculate with addition."""
        response = self.client.post("/api/calculate", json={
            "operation": "+",
            "a": 25.0,
            "b": 25.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "success",
            "operation": "+",
            "result": 50.0
        })

    def test_successful_multiplication(self):
        """Test POST /api/calculate with multiplication."""
        response = self.client.post("/api/calculate", json={
            "operation": "*",
            "a": 10.0,
            "b": 10.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "success",
            "operation": "*",
            "result": 100.0
        })

    def test_division_by_zero_error(self):
        """Test division by zero returns 400 Bad Request."""
        response = self.client.post("/api/calculate", json={
            "operation": "/",
            "a": 10.0,
            "b": 0.0
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("detail", response.json())

    def test_square_root(self):
        """Test square root API calculation."""
        response = self.client.post("/api/calculate", json={
            "operation": "sqrt",
            "a": 16.0
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            "status": "success",
            "operation": "sqrt",
            "result": 4.0
        })

    def test_logarithm_validation(self):
        """Test invalid logarithm argument returns 400."""
        response = self.client.post("/api/calculate", json={
            "operation": "log",
            "a": -1.0
        })
        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()