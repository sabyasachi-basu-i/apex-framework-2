"""Health check endpoints for the intelligence service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/live")
async def live() -> dict:
    """Liveness probe."""
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    """Readiness probe.  In a real implementation this would check downstream
    dependencies such as the vector store or LLM provider."""
    return {"status": "ready"}