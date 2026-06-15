import unittest
from unittest.mock import patch
from backend.auth_service import AuthService
from backend.database import User

class TestAuthService(unittest.TestCase):
    """Unit tests for the User Authentication Service."""

    def setUp(self):
        self.auth_service = AuthService(secret_key="TEST_SECRET")
        self.test_email = "test@example.com"
        self.test_password = "securepassword123"

    def test_password_hashing_and_verification(self):
        """Test password hashing and verification utility functions."""
        hashed = self.auth_service.hash_password(self.test_password)
        self.assertNotEqual(hashed, self.test_password.encode('utf-8'))
        
        # Test valid password verification
        self.assertTrue(self.auth_service.verify_password(self.test_password, hashed))
        
        # Test invalid password verification
        self.assertFalse(self.auth_service.verify_password("wrongpassword", hashed))

    @patch('backend.auth_service.AuthService.get_user_by_email')
    @patch('backend.auth_service.AuthService.create_user')
    def test_successful_user_registration(self, mock_create_user, mock_get_user):
        """Test user registration is successful when email is unique."""
        mock_get_user.return_value = None
        mock_user = User(id=1, email=self.test_email, hashed_password=b"hashed")
        mock_create_user.return_value = mock_user

        user_id = self.auth_service.register_user(self.test_email, self.test_password)
        self.assertEqual(user_id, 1)

    @patch('backend.auth_service.AuthService.get_user_by_email')
    def test_failed_user_registration_duplicate_email(self, mock_get_user):
        """Test registration fails when email is already registered."""
        mock_get_user.return_value = User(id=1, email=self.test_email, hashed_password=b"hashed")
        
        user_id = self.auth_service.register_user(self.test_email, self.test_password)
        self.assertIsNone(user_id)

    @patch('backend.auth_service.AuthService.get_user_by_email')
    @patch('backend.auth_service.AuthService.verify_password')
    def test_successful_login(self, mock_verify, mock_get_user):
        """Test successful login returns a valid JWT token."""
        mock_user = User(id=42, email=self.test_email, hashed_password=b"hashed")
        mock_get_user.return_value = mock_user
        mock_verify.return_value = True

        token = self.auth_service.login_user(self.test_email, self.test_password)
        self.assertIsNotNone(token)

        # Decode token to verify user_id subject matches
        decoded = self.auth_service.decode_access_token(token)
        self.assertEqual(decoded["sub"], "42")

    @patch('backend.auth_service.AuthService.get_user_by_email')
    @patch('backend.auth_service.AuthService.verify_password')
    def test_failed_login_invalid_password(self, mock_verify, mock_get_user):
        """Test login fails when credentials/password mismatch."""
        mock_user = User(id=42, email=self.test_email, hashed_password=b"hashed")
        mock_get_user.return_value = mock_user
        mock_verify.return_value = False

        token = self.auth_service.login_user(self.test_email, "wrongpassword")
        self.assertIsNone(token)

    def test_jwt_token_decoding_and_validation(self):
        """Test JWT token generation, valid decoding, and error fallback."""
        token = self.auth_service.create_access_token(user_id=10)
        decoded = self.auth_service.decode_access_token(token)
        self.assertEqual(decoded["sub"], "10")

        # Test invalid token decode
        invalid = self.auth_service.decode_access_token("invalid_token_string")
        self.assertIsNone(invalid)

if __name__ == '__main__':
    unittest.main()