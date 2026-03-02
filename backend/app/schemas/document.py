from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: str
    filename: str
    file_type: str | None
    source: str | None
    total_chunks: int | None

    class Config:
        from_attributes = True


