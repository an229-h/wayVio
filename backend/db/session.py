import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 1. Safely pull the secrets from the .env file injected by Docker
POSTGRES_USER = os.getenv("POSTGRES_USER", "admin")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "fallback_if_missing")
POSTGRES_DB = os.getenv("POSTGRES_DB", "core_telemetry_store")

# 2. Hardcode only the architecture details, not the secrets
POSTGRES_HOST = "database"  # The exact name of the service in docker-compose.yml
POSTGRES_PORT = "5432"

# 3. Assemble the string dynamically
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session in our FastAPI endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()