from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.agents.react_agent import get_agent_response

router = APIRouter()

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await get_agent_response(request.message, request.history)
    return ChatResponse(response=response, session_id=request.session_id)
