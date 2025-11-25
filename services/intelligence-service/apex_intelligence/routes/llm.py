"""LLM completion endpoints."""

from fastapi import APIRouter, Depends
from apex_intelligence.core.llm_client import LLMClient
from apex_intelligence.models import CompletionRequest, CompletionResponse
from apex_intelligence.security import get_current_user

router = APIRouter()
client = LLMClient()


@router.post("/completions", response_model=CompletionResponse)
async def create_completion(req: CompletionRequest, _user: str = Depends(get_current_user)) -> CompletionResponse:
    completion = await client.complete(prompt=req.prompt, max_tokens=req.max_tokens)
    return CompletionResponse(completion=completion)
