# Templates for Coder Buddy to generate User Auth, Deployment, and Testing

TEMPLATES = {
    "auth_fastapi": """# FastAPI JWT User Authentication Template
# Requires packages: fastapi, passlib[bcrypt], pyjwt, pydantic, sqlalchemy (or similar)

from datetime import datetime, timedelta
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

# Configuration
SECRET_KEY = "your-secret-key-change-this-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
router = APIRouter(prefix="/auth", tags=["authentication"])

# Pydantic Schemas
class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# Mock database helper (Replace with SQL / Mongo query logic)
MOCK_USERS_DB = {}

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = MOCK_USERS_DB.get(token_data.username)
    if user is None:
        raise credentials_exception
    return UserResponse(username=user["username"], email=user["email"])

@router.post("/register", response_model=UserResponse)
def register(user_data: UserRegister):
    if user_data.username in MOCK_USERS_DB:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user_data.password)
    MOCK_USERS_DB[user_data.username] = {
        "username": user_data.username,
        "email": user_data.email,
        "hashed_password": hashed_password
    }
    return UserResponse(username=user_data.username, email=user_data.email)

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = MOCK_USERS_DB.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=UserResponse)
def read_users_me(current_user: UserResponse = Depends(get_current_user)):
    return current_user
""",

    "auth_flask": """# Flask User Authentication Template
# Requires packages: Flask, Werkzeug

from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Mock Database
MOCK_USERS_DB = {}

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    if username in MOCK_USERS_DB:
        return jsonify({"error": "Username already exists"}), 400

    MOCK_USERS_DB[username] = {
        "username": username,
        "email": email,
        "password_hash": generate_password_hash(password)
    }
    return jsonify({"message": "User registered successfully", "username": username}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')

    user = MOCK_USERS_DB.get(username)
    if not user or not check_password_hash(user['password_hash'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['username'] = username
    return jsonify({"message": "Login successful", "username": username}), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.pop('username', None)
    return jsonify({"message": "Logged out successfully"}), 200

@auth_bp.route('/me', methods=['GET'])
def get_me():
    username = session.get('username')
    if not username:
        return jsonify({"error": "Unauthorized"}), 401
    
    user = MOCK_USERS_DB.get(username)
    return jsonify({"username": user['username'], "email": user['email']}), 200
""",

    "auth_frontend": """<!-- Beautiful Glassmorphism Login & Signup UI -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authentication Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(255, 255, 255, 0.05);
            --card-border: rgba(255, 255, 255, 0.1);
            --primary-color: #3b82f6;
            --accent-color: #ec4899;
            --text-color: #f3f4f6;
            --text-muted: #9ca3af;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Outfit', sans-serif;
        }

        body {
            background: radial-gradient(circle at top right, #1e1b4b, var(--bg-color) 60%);
            color: var(--text-color);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow-x: hidden;
        }

        .auth-container {
            background: var(--card-bg);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid var(--card-border);
            border-radius: 24px;
            padding: 40px;
            width: 100%;
            max-width: 440px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .auth-header {
            text-align: center;
            margin-bottom: 30px;
        }

        .auth-header h1 {
            font-size: 2rem;
            font-weight: 600;
            background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }

        .auth-header p {
            color: var(--text-muted);
            font-size: 0.95rem;
        }

        .form-group {
            margin-bottom: 20px;
            position: relative;
        }

        .form-group label {
            display: block;
            margin-bottom: 8px;
            font-size: 0.85rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .form-input {
            width: 100%;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--card-border);
            border-radius: 12px;
            padding: 12px 16px;
            color: var(--text-color);
            font-size: 1rem;
            outline: none;
            transition: all 0.2s ease;
        }

        .form-input:focus {
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.15);
            background: rgba(255, 255, 255, 0.07);
        }

        .btn-submit {
            width: 100%;
            background: linear-gradient(135deg, var(--primary-color), #2563eb);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 14px;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            margin-top: 10px;
        }

        .btn-submit:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(59, 130, 246, 0.3);
        }

        .btn-submit:active {
            transform: translateY(0);
        }

        .auth-toggle {
            text-align: center;
            margin-top: 24px;
            font-size: 0.9rem;
            color: var(--text-muted);
        }

        .auth-toggle span {
            color: var(--primary-color);
            cursor: pointer;
            font-weight: 600;
            transition: color 0.2s;
        }

        .auth-toggle span:hover {
            color: var(--accent-color);
            text-decoration: underline;
        }

        .alert {
            padding: 12px 16px;
            border-radius: 12px;
            margin-bottom: 20px;
            font-size: 0.9rem;
            display: none;
        }

        .alert-error {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.2);
            color: #f87171;
        }

        .alert-success {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.2);
            color: #34d399;
        }
    </style>
</head>
<body>

<div class="auth-container" id="authContainer">
    <div class="auth-header">
        <h1 id="authTitle">Welcome Back</h1>
        <p id="authSubtitle">Please sign in to access your dashboard</p>
    </div>

    <div class="alert alert-error" id="authError"></div>
    <div class="alert alert-success" id="authSuccess"></div>

    <form id="authForm" onsubmit="handleAuth(event)">
        <div class="form-group" id="emailGroup" style="display: none;">
            <label for="email">Email Address</label>
            <input type="email" id="email" class="form-input" placeholder="you@example.com">
        </div>

        <div class="form-group">
            <label for="username">Username</label>
            <input type="text" id="username" class="form-input" placeholder="username" required>
        </div>

        <div class="form-group">
            <label for="password">Password</label>
            <input type="password" id="password" class="form-input" placeholder="••••••••" required>
        </div>

        <button type="submit" class="btn-submit" id="submitBtn">Sign In</button>
    </form>

    <div class="auth-toggle">
        <p id="toggleText">Don't have an account? <span onclick="toggleAuthMode()">Sign Up</span></p>
    </div>
</div>

<script>
    let isLoginMode = true;

    function toggleAuthMode() {
        isLoginMode = !isLoginMode;
        
        const title = document.getElementById('authTitle');
        const subtitle = document.getElementById('authSubtitle');
        const emailGroup = document.getElementById('emailGroup');
        const submitBtn = document.getElementById('submitBtn');
        const toggleText = document.getElementById('toggleText');
        const emailInput = document.getElementById('email');

        document.getElementById('authError').style.display = 'none';
        document.getElementById('authSuccess').style.display = 'none';

        if (isLoginMode) {
            title.textContent = 'Welcome Back';
            subtitle.textContent = 'Please sign in to access your dashboard';
            emailGroup.style.display = 'none';
            emailInput.removeAttribute('required');
            submitBtn.textContent = 'Sign In';
            toggleText.innerHTML = `Don't have an account? <span onclick="toggleAuthMode()">Sign Up</span>`;
        } else {
            title.textContent = 'Create Account';
            subtitle.textContent = 'Register a new account to get started';
            emailGroup.style.display = 'block';
            emailInput.setAttribute('required', 'true');
            submitBtn.textContent = 'Create Account';
            toggleText.innerHTML = `Already have an account? <span onclick="toggleAuthMode()">Sign In</span>`;
        }
    }

    async function handleAuth(event) {
        event.preventDefault();
        
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const errorDiv = document.getElementById('authError');
        const successDiv = document.getElementById('authSuccess');

        errorDiv.style.display = 'none';
        successDiv.style.display = 'none';

        let url = isLoginMode ? '/auth/login' : '/auth/register';
        let body = {};
        
        // Handle headers/params depending on FastAPI vs Flask standards
        let options = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' }
        };

        if (isLoginMode) {
            // For OAuth2PasswordRequestForm in FastAPI, it expects form-url-encoded or JSON.
            // Let's implement both JSON fallback and URL-encoded.
            const urlEncodedData = new URLSearchParams();
            urlEncodedData.append('username', username);
            urlEncodedData.append('password', password);
            
            options.headers['Content-Type'] = 'application/x-www-form-urlencoded';
            options.body = urlEncodedData;
        } else {
            const email = document.getElementById('email').value;
            body = { username, email, password };
            options.body = JSON.stringify(body);
        }

        try {
            const response = await fetch(url, options);
            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || data.error || 'Authentication failed');
            }

            if (isLoginMode) {
                // Save token to localStorage
                localStorage.setItem('access_token', data.access_token);
                localStorage.setItem('username', username);
                
                successDiv.textContent = 'Successfully logged in! Redirecting...';
                successDiv.style.display = 'block';
                
                setTimeout(() => {
                    window.location.href = '/dashboard.html';
                }, 1500);
            } else {
                successDiv.textContent = 'Account created successfully! Switching to sign in...';
                successDiv.style.display = 'block';
                setTimeout(() => {
                    toggleAuthMode();
                }, 1500);
            }

        } catch (err) {
            errorDiv.textContent = err.message;
            errorDiv.style.display = 'block';
        }
    }
</script>
</body>
</html>
""",

    "deploy_docker": """# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    libpq-dev \\
    && rm -rf /var/lib/apt/lists/*

# Install python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Expose port and declare startup command
EXPOSE 8000
CMD ["python", "backend/main.py"]

---
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MYSQL_HOST=db
      - MYSQL_DATABASE=coder_buddy
      - MYSQL_USER=root
      - MYSQL_PASSWORD=rootpassword
      - MONGO_URI=mongodb://mongo:27017/CoderBuddy
    depends_on:
      - db
      - mongo

  db:
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpassword
      MYSQL_DATABASE: coder_buddy
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql

  mongo:
    image: mongo:6.0
    restart: always
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db

volumes:
  mysql_data:
  mongo_data:
""",

    "deploy_render": """# render.yaml blueprint deployment configuration
services:
  # Python backend (FastAPI/Flask)
  - type: web
    name: coder-buddy-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: MYSQL_HOST
        value: localhost
      - key: MONGO_URI
        sync: false

  # Static Frontend
  - type: web
    name: coder-buddy-frontend
    env: static
    buildCommand: echo "Building frontend"
    publishPath: ./frontend
    headers:
      - path: /*
        headers:
          - key: Cache-Control
            value: max-age=0, must-revalidate
""",

    "deploy_vercel": """{
  "version": 2,
  "builds": [
    {
      "src": "backend/main.py",
      "use": "@vercel/python"
    },
    {
      "src": "frontend/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/auth/(.*)",
      "dest": "backend/main.py"
    },
    {
      "src": "/api/(.*)",
      "dest": "backend/main.py"
    },
    {
      "src": "/(.*)",
      "dest": "frontend/$1"
    }
  ]
}
""",

    "test_unittest": """# Basic Python Unittest Suite
import unittest
import json
from unittest.mock import patch, MagicMock

# Import your application modules here:
# from backend.main import app

class TestAuthenticationAPI(unittest.TestCase):
    def setUp(self):
        # Initialize test clients or state
        self.mock_user = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepassword123"
        }

    def test_mock_registration(self):
        # A simple placeholder unit test to verify auth assertions
        username = self.mock_user["username"]
        email = self.mock_user["email"]
        
        self.assertEqual(username, "testuser")
        self.assertIn("@", email)

    def test_json_payload_structure(self):
        payload = json.dumps(self.mock_user)
        loaded = json.loads(payload)
        
        self.assertEqual(loaded["username"], "testuser")
        self.assertTrue(len(loaded["password"]) >= 8)

if __name__ == "__main__":
    unittest.main()
"""
}
