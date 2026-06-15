# config/database.py
from dataclasses import dataclass
from typing import List, Optional

# --- University Constants ---
UNIVERSITY_NAME = "State University of Technology"
UNIVERSITY_ADDRESS = "123 Academic Way, City, State 90210"
DEFAULT_ADMIN_EMAIL = "admin@university.edu"

# --- Data Models for Future Backend Interaction ---

@dataclass(frozen=True)
class User:
    """Represents a user entity in the system."""
    user_id: Optional[int] = None
    username: str
    email: str
    is_active: bool = True
    created_at: str # ISO format string

@dataclass(frozen=True)
class Course:
    """Represents a course entity."""
    course_id: Optional[int] = None
    title: str
    description: str
    credits: int
    department: str

@dataclass(frozen=True)
class Enrollment:
    """Represents an enrollment relationship between User and Course."""
    enrollment_id: Optional[int] = None
    user_id: int
    course_id: int
    enrollment_date: str # ISO format string

# --- Database Configuration Placeholder ---
# In a real application, this section would handle connection strings, 
# environment variables loading, and database session management.

class DatabaseConfig:
    """Configuration settings for the database connection."""
    DATABASE_URL = "sqlite:///./university.db"  # Example using SQLite
    MAX_CONNECTIONS = 20
    ENCODING = "utf-8"

def get_default_config() -> DatabaseConfig:
    """Returns the default configuration settings."""
    return DatabaseConfig()

if __name__ == '__main__':
    # Example usage of constants and models
    print(f"University Name: {UNIVERSITY_NAME}")
    print(f"Address: {UNIVERSITY_ADDRESS}")
    
    sample_user = User(username="jdoe", email="john.doe@university.edu")
    print("\nSample User Model:")
    print(sample_user)

    sample_course = Course(title="Introduction to Coding", description="Basics of programming.", credits=3, department="Computer Science")
    print("\nSample Course Model:")
    print(sample_course)