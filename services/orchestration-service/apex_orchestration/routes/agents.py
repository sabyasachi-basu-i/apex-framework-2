"""Agent routes (placeholder)."""

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def list_agents() -> dict:
    """Return a list of agents.  Not implemented yet."""
    return {"agents": []}