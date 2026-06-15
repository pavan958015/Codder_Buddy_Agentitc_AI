# Technical Design: Core Data Models and API Contract

This document outlines the core data models using SQLAlchemy for PostgreSQL persistence and defines the corresponding Pydantic schemas for request/response validation, establishing the contract between the database layer and the FastAPI backend.

## 1. Database Schema (SQLAlchemy Models)

We define the core entities required for the application. This section assumes a basic `User` model as an example.

```python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

# Example of another potential model (e.g., Item)
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, default=0)
    user_id = Column(Integer, nullable=False) # Foreign key relationship

# Note: Alembic migrations will be used to manage schema changes based on these models.
```

## 2. Pydantic Schemas (Data Validation)

These schemas define the structure for data entering and leaving the API endpoints, ensuring type safety and validation using FastAPI's dependency injection capabilities.

### User Schemas

**Request Schema (Create/Update)**
Used when receiving data from the client.

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str # Plain text password for initial creation

class UserUpdate(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None
```

**Response Schema (Read)**
Used when returning data to the client. Note that sensitive fields like `hashed_password` are excluded from responses.

```python
class UserBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

class UserResponse(UserBase):
    # Password is intentionally omitted here
    pass
```

### Item Schemas

**Request Schema (Create)**

```python
class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: int
    user_id: int
```

**Response Schema (Read)**

```python
class ItemResponse(ItemBase):
    # Assuming ItemBase includes all fields from the DB model
    pass
```

## 3. FastAPI Endpoint Structure

The API structure will follow RESTful conventions, utilizing dependency injection for database session management and Pydantic models for request/response handling.

### User Endpoints

| Method | Path | Description | Request Schema | Response Schema | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST` | `/users/` | Create a new user | `UserCreate` | `UserResponse` | Requires authentication (if applicable) |
| `GET` | `/users/{user_id}` | Retrieve a specific user by ID | None | `UserResponse` | Returns 404 if not found |
| `PUT` | `/users/` | Update an existing user | `UserUpdate` | `UserResponse` | Partial update allowed |

### Item Endpoints

| Method | Path | Description | Request Schema | Response Schema | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `POST` | `/items/` | Create a new item | `ItemCreate` | `ItemResponse` | Requires authentication |
| `GET` | `/items/{item_id}` | Retrieve an item by ID | None | `ItemResponse` | Returns 404 if not found |
| `GET` | `/items/` | List all items (with optional pagination) | None | `ListItemsResponse` | Supports query parameters for filtering/pagination |

### Global Considerations

1.  **Authentication:** All write operations (`POST`, `PUT`) will require a JWT or session token, managed via FastAPI dependencies.
2.  **Error Handling:** Standardized HTTP exception handlers (e.g., 400 Bad Request for validation errors, 401 Unauthorized, 500 Internal Server Error) will be implemented globally.
3.  **Database Connection:** A dependency injection pattern will be used to provide a database session context across all routes.