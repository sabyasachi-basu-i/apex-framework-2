"""Run history endpoints (placeholder)."""

from fastapi import APIRouter

router = APIRouter()

# In-memory store of past flows (simple, not persisted)
_run_history: list[dict] = []


@router.get("")
async def list_runs() -> dict:
    """Return a list of past flow executions (empty placeholder)."""
    return {"runs": _run_history}