# Plug in your existing agent logic here
# From: framework-free-agent or agentic-systems-with-langgraph

from typing import AsyncGenerator

async def get_agent_response(message: str, history: list) -> str:
    # TODO: Connect your LangGraph / ReAct agent
    return f"Agent response to: {message}"

async def stream_agent_response(message: str, history: list) -> AsyncGenerator[str, None]:
    # TODO: Connect your streaming LangGraph agent
    words = f"Streaming response to: {message}".split()
    for word in words:
        yield f"data: {word} \n\n"

