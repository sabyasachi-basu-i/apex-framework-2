"""LLM completion endpoints."""

from fastapi import APIRouter
from apex_intelligence.core.llm_client import LLMClient
from apex_intelligence.models import CompletionRequest, CompletionResponse

router = APIRouter()
client = LLMClient()


@router.post("/completions", response_model=CompletionResponse)
async def create_completion(req: CompletionRequest) -> CompletionResponse:
    """Generate a completion for the given prompt.  This implementation
    simply echoes the prompt back.  Replace with calls to your provider
    of choice (OpenAI, Azure, Groq, etc.)."""
    completion = await client.complete(prompt=req.prompt, max_tokens=req.max_tokens)
    return CompletionResponse(completion=completion)