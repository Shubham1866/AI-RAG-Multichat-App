from sqlalchemy.orm import Session
from app.models.chat import Chat


def delete_chat_by_id(db: Session, chat_id: str):
    chat = db.query(Chat).filter(Chat.id == chat_id).first()

    if not chat:
        return False

    db.delete(chat)
    db.commit()
    return True
