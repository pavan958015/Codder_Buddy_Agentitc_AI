from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for all models
Base = declarative_base()

class User(Base):
    """
    SQLAlchemy model representing a user in the database.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)

class MemoryState(Base):
    """
    SQLAlchemy model representing user memory state or preferences.
    This can be used to store session-specific data or application context.
    """
    __tablename__ = "memory_states"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True, nullable=False) # Foreign key relationship would be ideal in a full setup
    state_data = Column(String(256), nullable=True)
    updated_at = Column(String(50))

# Example setup (This part would typically be in a separate database configuration file)
# engine = create_engine("sqlite:///./test.db")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

if __name__ == '__main__':
    print("SQLAlchemy models defined successfully.")