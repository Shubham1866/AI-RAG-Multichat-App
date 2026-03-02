from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import os

from app.core.dependencies import get_db
# from app.services.document_ingestion import ingest_document
from app.models.document import Document
from app.services.document_ingestion import ingest_document

router = APIRouter(prefix="/ingestion", tags=["Ingestion"])
UPLOAD_DIR = "uploads/documents"


@router.post("/run")
def run_ingestion(db: Session = Depends(get_db)):
    pending_docs = (
        db.query(Document)
        .filter(Document.embedding_status == "PENDING")
        .limit(5)  # IMPORTANT: batch control
        .all()
    )

    processed = []

    for doc in pending_docs:
        try:
            doc.embedding_status = "PROCESSING"
            db.commit()

            file_path = os.path.join(UPLOAD_DIR, doc.filename)
            total_chunks = ingest_document(file_path, doc.id)

            doc.total_chunks = total_chunks
            doc.embedding_status = "COMPLETED"
            doc.embedding_error = None
            db.commit()

            processed.append(doc.id)

        except Exception as e:
            doc.embedding_status = "FAILED"
            doc.embedding_error = str(e)[:500]
            db.commit()

    return {
        "processed_documents": processed,
        "count": len(processed)
    }