import uuid
from sqlalchemy.orm import Session
from app.models.document import Document


def create_document(
    db: Session,
    filename: str,
    file_type: str | None = None,
    source: str | None = "upload"
):
    db_document = Document(
        id=str(uuid.uuid4()),
        filename=filename,
        file_type=file_type,
        source=source,
        total_chunks=0,
        embedding_status="PENDING"
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document