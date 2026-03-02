import os
import shutil
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.models.user import User
from app.core.dependencies import get_db
from app.crud.document import create_document
from app.schemas.document import DocumentResponse

UPLOAD_DIR = "uploads/documents"

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload", response_model=DocumentResponse, status_code=status.HTTP_201_CREATED)
def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if not file.filename:
        raise HTTPException(status_code=400, detail="Invalid file")

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Prevent overwrite
    if os.path.exists(file_path):
        raise HTTPException(
            status_code=400,
            detail="File already exists"
        )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = create_document(
        db=db,
        filename=file.filename,
        file_type=file.content_type,
        source="upload"
    )

    return document