from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:Shubham1866@localhost:3306/rag_chat_db"

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