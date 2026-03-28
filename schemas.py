from pydantic import BaseModel
from typing import Optional, List

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    history: Optional[List[dict]] = []

class ChatResponse(BaseModel):
    response: str
    session_id: Optional[str] = None

class UploadResponse(BaseModel):
    filename: str
    status: str
    message: str
