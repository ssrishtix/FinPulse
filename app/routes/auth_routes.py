from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import timedelta

from app.database import get_db
from app.models import User
from app.schemas import UserLogin
from app.utils import verify_password
from app.auth import create_access_token
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/login")
def login(user_cred: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_cred.email).first()
    if not user or not verify_password(user_cred.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }
