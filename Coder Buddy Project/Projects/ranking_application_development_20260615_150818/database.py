from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base class for all models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, default=0)
    user_id = Column(Integer, nullable=False) # Foreign key relationship

# Setup for database session (to be configured in main.py or environment variables)
engine = None
SessionLocal = sessionmaker()

def init_db():
    """Initializes the database and creates tables."""
    global engine
    from sqlalchemy import create_engine
    # In a real application, this would connect to PostgreSQL using an environment variable
    # For now, we use SQLite in-memory for demonstration purposes.
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)

def get_db():
    """Dependency function to provide a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()