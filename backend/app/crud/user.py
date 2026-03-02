from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserRegister
from app.core.security import hash_password
import uuid


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserRegister):
    db_user = User(
        id=str(uuid.uuid4()),
        name=user.name,
        email=user.email,
        password_hash=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user