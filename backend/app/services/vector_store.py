import faiss
import numpy as np
import os
import pickle

VECTOR_DIR = "vector_store"
INDEX_PATH = os.path.join(VECTOR_DIR, "index.faiss")
META_PATH = os.path.join(VECTOR_DIR, "metadata.pkl")


def _load_index(dim: int):
    os.makedirs(VECTOR_DIR, exist_ok=True)

    if os.path.exists(INDEX_PATH):
        index = faiss.read_index(INDEX_PATH)
        with open(META_PATH, "rb") as f:
            metadata = pickle.load(f)
    else:
        index = faiss.IndexFlatL2(dim)
        metadata = []

    return index, metadata


def _save_index(index, metadata):
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(metadata, f)


def store_embeddings(
    embeddings: list[list[float]],
    metadatas: list[dict]
):
    """
    Appends embeddings and metadata to FAISS index.
    """
    if not embeddings:
        return

    vectors = np.array(embeddings).astype("float32")
    index, metadata = _load_index(vectors.shape[1])

    index.add(vectors)
    metadata.extend(metadatas)

    _save_index(index, metadata)