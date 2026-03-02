import uuid
from sqlalchemy.orm import Session
from app.models.message import Message


def create_message(db: Session, chat_id: str, role: str, content: str):
    msg = Message(
        id=str(uuid.uuid4()),
        chat_id=chat_id,
        role=role,
        content=content
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def get_chat_history(db: Session, chat_id: str, limit: int = 10):
    messages = (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
        .limit(limit)
        .all()
    )

    return [
        {"role": m.role, "content": m.content}
        for m in messages
    ]