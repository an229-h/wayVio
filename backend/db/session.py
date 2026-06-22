import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Get the database URL from the environment variables (set in Docker)
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Create the engine that establishes the actual connection
engine = create_engine(DATABASE_URL)

# 3. Create a factory for individual "sessions" (like a single trip to the pantry)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. A helper function for FastAPI to open and safely close a pantry trip
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()