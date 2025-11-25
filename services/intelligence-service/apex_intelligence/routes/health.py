"""Health check endpoints for the intelligence service."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict:
    return {"status": "healthy"}


@router.get("/live")
async def live() -> dict:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    return {"status": "ready"}
