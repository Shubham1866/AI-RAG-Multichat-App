from pypdf import PdfReader
import os

def clean_text(text: str) -> str:
    return text.encode("utf-8", "ignore").decode("utf-8")


def read_document(file_path: str) -> str:
    """
    Reads document content and returns extracted text.
    Currently supports PDF only.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError("Document not found")

    if file_path.lower().endswith(".pdf"):
        return clean_text(_read_pdf(file_path))
    elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                return clean_text(f.read())

    raise ValueError("Unsupported file type")


def _read_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    pages_text = []

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages_text.append(text)

    return "\n".join(pages_text)