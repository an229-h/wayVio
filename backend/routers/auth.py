from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from db.session import get_db
from models.user import User
from schemas.auth import UserCreate, UserResponse

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

# This sets up our secure password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if the email already exists in the pantry
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Securely scramble the password
    hashed_password = pwd_context.hash(user.password)

    # 3. Build the new user object
    new_user = User(email=user.email, password_hash=hashed_password)
    
    # 4. Save it to the database pantry
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user