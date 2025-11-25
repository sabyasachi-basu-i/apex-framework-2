"""Configuration endpoints for integration service."""
from fastapi import APIRouter, Depends

from apex_integration.config import load_config, update_config
from apex_integration.security import get_current_user

router = APIRouter()


@router.get("/")
async def get_config(_user: str = Depends(get_current_user)) -> dict:
    cfg = load_config()
    return cfg.dict()


@router.post("/")
async def save_config(payload: dict, _user: str = Depends(get_current_user)) -> dict:
    cfg = update_config(payload)
    return cfg.dict()
