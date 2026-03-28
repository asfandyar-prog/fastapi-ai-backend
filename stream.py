from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.schemas import ChatRequest
from app.agents.react_agent import stream_agent_response

router = APIRouter()

@router.post("/")
async def stream(request: ChatRequest):
    return StreamingResponse(
        stream_agent_response(request.message, request.history),
        media_type="text/event-stream"
    )
