from app.services.document_reader import read_document
from app.services.text_chunker import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.vector_store import store_embeddings


def ingest_document(
    file_path: str,
    document_id: str
) -> int:
    """
    Full ingestion pipeline:
    read → chunk → embed → store
    """
    text = read_document(file_path)

    if not text.strip():
        raise ValueError("Document has no readable text")

    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    metadatas = [
        {
            "document_id": document_id,
            "chunk_index": idx,
            "text": chunk
        }
        for idx, chunk in enumerate(chunks)
    ]

    store_embeddings(embeddings, metadatas)

    return len(chunks)