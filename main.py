from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chat, stream, upload
from app.core.config import settings

app = FastAPI(
    title="FastAPI AI Backend",
    description="Production-grade AI agent backend with streaming, RAG, and multi-agent support.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(stream.router, prefix="/stream", tags=["Stream"])
app.include_router(upload.router, prefix="/upload", tags=["Upload"])

@app.get("/")
async def root():
    return {"status": "running", "message": "FastAPI AI Backend is live."}
