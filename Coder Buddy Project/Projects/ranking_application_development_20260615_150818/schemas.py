from pydantic import BaseModel, EmailStr
from typing import Optional

# --- User Schemas ---

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str # Plain text password for initial creation

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None

class UserBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

class UserResponse(UserBase):
    # Password is intentionally omitted here
    pass

# --- Item Schemas ---

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    user_id: int

class ItemResponse(BaseModel):
    # Assuming ItemBase includes all fields from the DB model
    pass