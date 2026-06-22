from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext
#AI
# Import your database session and the SQLAlchemy User model
from db.session import get_db
from models.user import User

# Import your Pydantic schemas
from schemas.auth import UserCreate, UserLogin, UserResponse

router = APIRouter(prefix="/api/v1/auth", tags=["auth"])

# Initialize the bcrypt password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    # 1. Check if the email is already in the database
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Hash the plain-text password from the request
    hashed_password = pwd_context.hash(user.password)

    # 3. Create the new User object
    new_user = User(
        email=user.email,
        password_hash=hashed_password
    )
    
    # 4. Save it to PostgreSQL
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # 5. Return the database object. FastAPI automatically filters out the 
    # password_hash and returns only what is in UserResponse!
    return new_user

@router.post("/login")
async def login(user: UserLogin, db: Session = Depends(get_db)):
    # We will build the JWT generation here next!
    return {"access_token": "your-jwt-token-here", "token_type": "bearer"}