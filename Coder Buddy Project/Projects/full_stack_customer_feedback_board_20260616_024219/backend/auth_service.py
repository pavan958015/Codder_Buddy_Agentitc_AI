import bcrypt
import jwt
from datetime import datetime, timedelta
from typing import Optional

# Assuming database models and session management utilities are imported from backend.database
# We assume a User model exists with fields like id, email, hashed_password.
# pyrefly: ignore [missing-import]
from backend.database import User  # Placeholder for actual DB model interaction functions

class AuthService:
    """
    Handles all user authentication logic including registration, login, 
    token management, and dependency injection setup.
    """
    def __init__(self, secret_key: str = "YOUR_SUPER_SECRET_KEY"):
        self.secret_key = secret_key

    # --- Password Hashing Utilities ---

    def hash_password(self, password: str) -> bytes:
        """Hashes a plaintext password using bcrypt."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt)

    def verify_password(self, plain_password: str, hashed_password: bytes) -> bool:
        """Verifies a plaintext password against a hashed password."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

    # --- User Model Interaction Functions (Simulated/Assumed DB interaction) ---

    def create_user(self, email: str, password: str) -> Optional[User]:
        """Creates a new user in the database after hashing the password."""
        hashed_password = self.hash_password(password)
        try:
            # In a real application, this would interact with SQLAlchemy/DB session
            new_user = User(email=email, hashed_password=hashed_password)
            # Simulate saving to DB
            print(f"User {email} created successfully.")
            return new_user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Retrieves a user from the database by their email."""
        # In a real application, this would query the DB
        print(f"Attempting to retrieve user with email: {email}")
        # Mock implementation for demonstration purposes
        if email == "test@example.com":
            return User(id=1, email="test@example.com", hashed_password=b"$2b$10$xxxxxxxxxxxxxx") # Mock hash
        return None

    # --- JWT Token Logic ---

    def create_access_token(self, user_id: int) -> str:
        """Generates a JWT access token for the given user ID."""
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=30),  # Token expires in 30 minutes
            "sub": str(user_id)
        }
        token = jwt.encode(payload, self.secret_key, algorithm="HS256")
        return token

    def decode_access_token(self, token: str) -> Optional[dict]:
        """Decodes and validates a JWT access token."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
            return None
        except jwt.InvalidTokenError:
            print("Invalid token provided.")
            return None

    # --- Authentication Flows ---

    def register_user(self, email: str, password: str) -> Optional[str]:
        """Handles user registration and returns the created user or None."""
        if not self.get_user_by_email(email):
            user = self.create_user(email, password)
            return user.id if user else None
        else:
            print("Error: User with this email already exists.")
            return None

    def login_user(self, email: str, password: str) -> Optional[str]:
        """Authenticates a user and returns an access token."""
        user = self.get_user_by_email(email)
        if not user or not self.verify_password(password, user.hashed_password):
            print("Error: Invalid credentials.")
            return None

        token = self.create_access_token(user.id)
        return token

    # --- Dependency Injection Setup (For FastAPI/Flask routes) ---

    def get_current_user_from_token(self, token: str) -> Optional[User]:
        """Dependency function to extract user info from the JWT token."""
        payload = self.decode_access_token(token)
        if payload and 'sub' in payload:
            # In a real app, you would fetch the full User object here using payload['sub']
            return User(id=payload['sub'], email="user@example.com", hashed_password=b"mock_hash") # Mock return
        return None

    def get_auth_dependency(self, token: str) -> Optional[User]:
        """A higher-order function or dependency wrapper for route protection."""
        return self.get_current_user_from_token(token)


# Example Usage (for testing purposes)
if __name__ == '__main__':
    auth_service = AuthService()

    print("--- Testing Password Hashing ---")
    plain_pass = "securepassword123"
    hashed = auth_service.hash_password(plain_pass)
    print(f"Hashed password (bytes): {hashed}")
    is_valid = auth_service.verify_password("securepassword123", hashed)
    print(f"Verification successful: {is_valid}\n")

    print("--- Testing Registration ---")
    new_user_id = auth_service.register_user("test@example.com", "securepassword123")
    if new_user_id:
        print(f"Registration result (User ID): {new_user_id}\n")

    print("--- Testing Login ---")
    token = auth_service.login_user("test@example.com", "securepassword123")
    if token:
        print(f"Login successful! Token generated: {token[:50]}...\n")
        decoded = auth_service.decode_access_token(token)
        print(f"Decoded payload: {decoded}")

        # --- Testing Dependency Injection Setup ---
        print("\n--- Testing Protected Route Dependency ---")
        user_info = auth_service.get_auth_dependency(token)
        if user_info:
            print("Dependency injection successful! User retrieved.")
        else:
            print("Dependency injection failed!")

    # Test invalid login
    invalid_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwR..."
    auth_service.login_user("test@example.com", "wrongpassword")