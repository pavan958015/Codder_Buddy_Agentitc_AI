import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

class Settings:
    """
    Application settings and configuration variables.
    Loads values from environment variables, providing sensible defaults 
    where applicable or raising errors for critical missing ones.
    """
    
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # Authentication Secret Key (Crucial for security)
    SECRET_KEY: str = os.getenv("SECRET_KEY", "a-very-insecure-default-key-change-me")
    
    # Application Settings
    DEBUG: bool = os.getenv("DEBUG", "True").lower() in ('true', '1', 't')
    APP_NAME: str = os.getenv("APP_NAME", "CalculatorApp")
    
    # Server Configuration (Example)
    PORT: int = int(os.getenv("PORT", 8000))

# Instantiate the settings object for easy access throughout the application
config = Settings()

if __name__ == '__main__':
    print(f"--- Application Configuration Loaded ---")
    print(f"App Name: {config.APP_NAME}")
    print(f"Debug Mode: {config.DEBUG}")
    print(f"Database URL: {config.DATABASE_URL}")
    # Note: In a real application, NEVER print the SECRET_KEY in production logs.
    print(f"Secret Key Loaded (first 10 chars): {config.SECRET_KEY[:10]}...")