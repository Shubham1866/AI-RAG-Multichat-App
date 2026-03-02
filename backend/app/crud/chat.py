import uuid
from sqlalchemy.orm import Session
from app.models.chat import Chat


def create_chat(
    db: Session,
    user_id: str,
    title: str | None
):
    chat = Chat(
        id=str(uuid.uuid4()),
        user_id=user_id,
        title=title
    )
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat