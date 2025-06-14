from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FinPulse API"}

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from init_db import Base, engine, get_db, User
from pydantic import BaseModel
from app.utils import hash_password
from fastapi.security import OAuth2PasswordRequestForm
from app.utils import verify_password

app = FastAPI()

# Create a Pydantic model for request validation
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_pw)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == form_data.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    return {"message": "Login successful", "user": user.email}
from fastapi import FastAPI
from app.routes import auth_routes, users  # users route from Day 1

app = FastAPI()

app.include_router(users.router)
app.include_router(auth_routes.router)

