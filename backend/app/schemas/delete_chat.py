from pydantic import BaseModel


class ChatDeleteResponse(BaseModel):
    message: str
    deleted_chat_id: str  # MUST be str (your IDs are UUID strings)