from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# --- Pydantic Schemas ---

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

class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    user_id: int

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int


class ListItemsResponse(BaseModel):
    items: List[ItemResponse]


# --- Mock Database/Service Layer (For demonstration purposes) ---
# In a real application, this would interact with SQLAlchemy models and a database session.

fake_users = {}
fake_items = {}
next_user_id = 1
next_item_id = 1

def get_db():
    """Mock dependency for database session."""
    print("Database session provided.")
    # In a real app: yield Session()
    try:
        yield True
    finally:
        print("Database session closed.")

# --- FastAPI Application Setup ---

app = FastAPI(title="Ranking Application API")

# --- User Endpoints ---

@app.post("/users/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate):
    global next_user_id
    new_user = {
        "id": next_user_id,
        "username": user_data.username,
        "email": user_data.email,
        "is_active": True
    }
    fake_users[next_user_id] = new_user
    next_user_id += 1
    return UserResponse(**new_user)

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse(**fake_users[user_id])

@app.put("/users/", response_model=UserResponse)
def update_user(user_data: UserUpdate, user_id: int):
    if user_id not in fake_users:
        raise HTTPException(status_code=404, detail="User not found")

    user = fake_users[user_id]
    update_data = user.copy()

    if user_data.username is not None:
        update_data["username"] = user_data.username
    if user_data.email is not None:
        update_data["email"] = user_data.email
    if user_data.is_active is not None:
        update_data["is_active"] = user_data.is_active

    fake_users[user_id] = update_data
    return UserResponse(**update_data)


# --- Item Endpoints ---

@app.post("/items/", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item_data: ItemCreate):
    global next_item_id
    new_item = {
        "id": next_item_id,
        "name": item_data.name,
        "description": item_data.description,
        "price": item_data.price,
        "user_id": item_data.user_id
    }
    fake_items[next_item_id] = new_item
    next_item_id += 1
    return ItemResponse(**new_item)

@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    if item_id not in fake_items:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**fake_items[item_id])

@app.get("/items/", response_model=ListItemsResponse)
def list_items():
    # In a real scenario, this would involve pagination and filtering logic
    return ListItemsResponse(items=list(fake_items.values()))

# --- Global Error Handler (Simplified for example) ---
@app.exception_handler(404)
async def http_exception_handler(request, exc):
    return {"detail": str(exc)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)