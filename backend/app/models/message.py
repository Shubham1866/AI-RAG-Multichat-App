from sqlalchemy import Column, String, Text, TIMESTAMP, ForeignKey, Enum, text
from app.core.database import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(String(36), primary_key=True)
    chat_id = Column(String(36), ForeignKey("chats.id", ondelete="CASCADE"))
    role = Column(Enum("user", "assistant", "system"), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))