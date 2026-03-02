from sqlalchemy import Column, String, Integer, TIMESTAMP, text, Enum
from app.core.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(String(36), primary_key=True)
    filename = Column(String(255), nullable=False)
    file_type = Column(String(50))
    source = Column(String(100))
    total_chunks = Column(Integer)
    embedding_status = Column(
        Enum("PENDING", "PROCESSING", "COMPLETED", "FAILED"),
        default="PENDING"
    )
    embedding_error = Column(String(500))
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))