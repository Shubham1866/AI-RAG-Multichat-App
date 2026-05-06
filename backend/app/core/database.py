from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "YOUR DATABASE CONNECTION URL"

#Connection
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

#Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
