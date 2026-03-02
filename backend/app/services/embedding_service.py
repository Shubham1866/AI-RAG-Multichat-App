import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

EMBEDDING_MODEL = "text-embedding-3-small"


def generate_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generates embeddings for a list of text chunks.
    """
    if not texts:
        return []

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    return [item.embedding for item in response.data]