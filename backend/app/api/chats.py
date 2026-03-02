from fastapi import APIRouter, Depends, status,HTTPException
from sqlalchemy.orm import Session

from app.schemas.chat import ChatCreate, ChatResponse
from app.crud.chat import create_chat
from app.core.dependencies import get_db
from app.core.auth import get_current_user
from typing import List
from app.schemas.chat import ChatListResponse
from app.models.chat import Chat
from app.models.user import User
from app.crud.delete_chat import delete_chat_by_id
from app.schemas.delete_chat import ChatDeleteResponse

router = APIRouter(prefix="/chats", tags=["Chats"])

@router.get(
    "/",
    response_model=List[ChatListResponse]
)
def list_chats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    chats = (
        db.query(Chat)
        .filter(Chat.user_id == current_user.id)
        .order_by(Chat.updated_at.desc())
        .all()
    )
    return chats

@router.post(
    "/start",
    response_model=ChatResponse,
    status_code=status.HTTP_201_CREATED
)
def start_chat(
    payload: ChatCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    chat = create_chat(
        db=db,
        user_id=current_user.id,
        title=payload.title
    )
    return chat


@router.delete("/{chat_id}", response_model=ChatDeleteResponse, status_code=status.HTTP_200_OK)
def delete_chat(chat_id: str, db: Session = Depends(get_db)):
   
    deleted = delete_chat_by_id(db, chat_id)
    if deleted:
        return {
            "message": "Chat deleted successfully",
            "deleted_chat_id": chat_id
        }
    else:
        raise HTTPException(status_code=404, detail="Chat not found")

