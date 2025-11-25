"""Chat orchestration endpoint for testing agents."""
from __future__ import annotations

import asyncio
from datetime import datetime
from typing import AsyncGenerator

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from apex_orchestration.security import get_current_user

router = APIRouter()


async def _chat_stream(message: str) -> AsyncGenerator[bytes, None]:
    chunks = ["Processing", " agent", " response", "..."]
    for chunk in chunks:
        await asyncio.sleep(0.1)
        yield f"data: {chunk}\n\n".encode()
    timestamp = datetime.utcnow().isoformat()
    yield f"data: {{\"message\": \"Echo: {message}\", \"timestamp\": \"{timestamp}\"}}\n\n".encode()


@router.post("/chat")
async def chat(payload: dict, stream: bool = False, _user: str = Depends(get_current_user)):
    message = payload.get("message", "")
    if stream:
        return StreamingResponse(_chat_stream(message), media_type="text/event-stream")
    timestamp = datetime.utcnow().isoformat()
    return {"message": f"Echo: {message}", "timestamp": timestamp}
