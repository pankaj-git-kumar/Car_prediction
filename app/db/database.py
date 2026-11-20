# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
# )

# SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base = declarative_base()

# def get_db():
#     """FastAPI dependency: one session per request, always closed afterwards."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Car_prediction folder (this file is Car_prediction/app/db/database.py)
BASE_DIR = Path(__file__).resolve().parents[2]

# Load Car_prediction/.env no matter where uvicorn is started from
load_dotenv(BASE_DIR / ".env")

# Use DATABASE_URL (server database). If missing, fall back to a local SQLite file.
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL") or f"sqlite:///{BASE_DIR / 'test.db'}"

# Some hosts give "postgres://..." but SQLAlchemy needs "postgresql://..."
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace(
        "postgres://", "postgresql://", 1
    )

# check_same_thread is needed for SQLite only
connect_args = (
    {"check_same_thread": False}
    if SQLALCHEMY_DATABASE_URL.startswith("sqlite")
    else {}
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,  # reconnects if the server closed an idle connection
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


def get_db():
    """FastAPI dependency: one session per request, always closed afterwards."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()