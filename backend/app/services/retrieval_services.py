import faiss
import pickle
import numpy as np
import os
from app.services.embedding_service import generate_embeddings

VECTOR_DIR = "vector_store"
INDEX_PATH = os.path.join(VECTOR_DIR, "index.faiss")
META_PATH = os.path.join(VECTOR_DIR, "metadata.pkl")


def retrieve_top_k(query: str, k: int = 5) -> list[str]:
    if not os.path.exists(INDEX_PATH):
        return []

    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        metadata = pickle.load(f)

    query_embedding = generate_embeddings([query])[0]
    query_vector = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_vector, k)

    results = []
    for idx in indices[0]:
        if idx < len(metadata):
            results.append(metadata[idx]["text"])

    return results