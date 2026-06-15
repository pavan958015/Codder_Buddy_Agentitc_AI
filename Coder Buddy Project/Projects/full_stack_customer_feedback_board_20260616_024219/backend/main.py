from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated

# pyrefly: ignore [missing-import]
from database import get_db, init_db, User, Feedback
# pyrefly: ignore [missing-import]
from auth_service import AuthService

app = FastAPI(title="Customer Feedback Board API")

# Enable CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth_service = AuthService()

# Initialize Database on startup
@app.on_event("startup")
async def startup_event():
    init_db()
    print("Database tables initialized.")

# --- Endpoints ---

@app.post("/auth/register", status_code=status.HTTP_201_CREATED)
def register(email: str, password: str, db: Session = Depends(get_db)):
    # Check if user already exists
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already registered")
    
    # Register user via auth service
    hashed = auth_service.hash_password(password)
    user = User(email=email, hashed_password=hashed)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully", "user_id": user.id}

@app.post("/auth/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not auth_service.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    token = auth_service.create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

# protected dependency
def get_current_user(token: str, db: Session = Depends(get_db)):
    payload = auth_service.decode_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = int(payload["sub"])
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.get("/feedback")
def list_feedback(db: Session = Depends(get_db)):
    feedbacks = db.query(Feedback).all()
    return feedbacks

@app.post("/feedback")
def add_feedback(content: str, rating: int, token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    feedback = Feedback(user_id=user.id, content=content, rating=rating)
    db.add(feedback)
    db.commit()
    db.refresh(feedback)
    return {"message": "Feedback submitted successfully", "id": feedback.id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)