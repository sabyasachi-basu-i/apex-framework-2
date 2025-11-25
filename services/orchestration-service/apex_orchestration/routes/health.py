"""Health endpoints."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health_root() -> dict:
    return {"status": "healthy"}


@router.get("/live")
async def live() -> dict:
    return {"status": "ok"}


@router.get("/ready")
async def ready() -> dict:
    return {"status": "ready"}
