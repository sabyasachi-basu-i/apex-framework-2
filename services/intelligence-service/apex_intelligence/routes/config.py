"""Configuration endpoints for runtime settings."""
from fastapi import APIRouter, Depends

from apex_intelligence.config import load_config, update_config
from apex_intelligence.models import ConfigResponse
from apex_intelligence.security import get_current_user

router = APIRouter()


@router.get("/", response_model=ConfigResponse)
async def get_config(_user: str = Depends(get_current_user)) -> ConfigResponse:
    cfg = load_config()
    return ConfigResponse(**cfg.dict())


@router.post("/", response_model=ConfigResponse)
async def save_config(payload: ConfigResponse, _user: str = Depends(get_current_user)) -> ConfigResponse:
    cfg = update_config(payload.dict())
    return ConfigResponse(**cfg.dict())
