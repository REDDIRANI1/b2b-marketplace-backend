from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct DB connection string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Incorrect%40123@localhost:5432/b2b_marketplace"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ Add this to make DB session injectable in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
