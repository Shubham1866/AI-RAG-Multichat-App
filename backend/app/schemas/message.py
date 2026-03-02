from pydantic import BaseModel
from datetime import datetime

class AskQuestionRequest(BaseModel):
    chat_id: str
    question: str

class MessageResponse(BaseModel):
    id: str
    role: str
    content: str
    created_at: datetime

    class Config:
        from_attributes = True