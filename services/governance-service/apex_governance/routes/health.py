"""Health endpoints for governance service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/live")
async def live() -> dict:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    return {"status": "ready"}