from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.message import MessageResponse
from app.models.message import Message
from app.core.dependencies import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.chat import Chat
from app.crud.message import create_message, get_chat_history
from app.schemas.message import AskQuestionRequest
from app.services.retrieval_services import retrieve_top_k
from app.services.prompt_builder import build_prompt
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/messages", tags=["Messages"])


@router.post("/ask")
def ask_question(
    payload: AskQuestionRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # 1️⃣ Validate chat ownership
    chat = db.query(Chat).filter(
        Chat.id == payload.chat_id,
        Chat.user_id == current_user.id
    ).first()

    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    # 2️⃣ Store user message
    create_message(db, payload.chat_id, "user", payload.question)

    # 3️⃣ Retrieve context
    context_chunks = retrieve_top_k(payload.question)

    # 4️⃣ Load chat history
    history = get_chat_history(db, payload.chat_id)

    # 5️⃣ Build prompt
    messages = build_prompt(
        question=payload.question,
        context_chunks=context_chunks,
        chat_history=history
    )

    # 6️⃣ Generate answer
    answer = generate_answer(messages)

    # 7️⃣ Store assistant message
    create_message(db, payload.chat_id, "assistant", answer)

    return {
        "answer": answer,
        "context_used": len(context_chunks)
    }


@router.get(
    "/chat/{chat_id}",
    response_model=List[MessageResponse]
)
def get_chat_messages(
    chat_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Validate chat ownership
    chat = (
        db.query(Chat)
        .filter(Chat.id == chat_id, Chat.user_id == current_user.id)
        .first()
    )

    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    messages = (
        db.query(Message)
        .filter(Message.chat_id == chat_id)
        .order_by(Message.created_at.asc())
        .all()
    )

    return messages