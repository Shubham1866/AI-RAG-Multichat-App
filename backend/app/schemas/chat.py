from pydantic import BaseModel
from datetime import datetime


class ChatCreate(BaseModel):
    title: str | None = "New Chat"


class ChatResponse(BaseModel):
    id: str
    title: str

    class Config:
        from_attributes = True

class ChatListResponse(BaseModel):
    id: str
    title: str | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True