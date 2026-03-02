from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.users import router as user_router
from app.api.documents import router as document_router
from app.api.ingestion import router as ingestion_router
from app.api.chats import router as chats_router
from app.api.messages import router as messages_router
from app.models import user, message,chat,document


app = FastAPI(
    title="RAG Based Multi-Chat System",
    description="FastAPI backend for RAG-based multi-user chat application",
    version="0.1.0"
)


# ✅ Allowed frontend URLs
ALLOWED_ORIGINS = [
    "http://localhost:5173",     # React (local)
    "http://127.0.0.1:5173",
    "https://yourdomain.com",    # Production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],        # Authorization, Content-Type, etc.
)

# To create tables automatically, run once
# @app.on_event("startup")
# def create_tables():
#     Base.metadata.create_all(bind=engine)


app.include_router(user_router)
app.include_router(document_router)
app.include_router(ingestion_router)
app.include_router(chats_router)
app.include_router(messages_router)
@app.get("/")
def root():
    return {
        "status": "success",
        "message": "RAG Multi-Chat API is running"
    }

