"""Authentication routes."""
from __future__ import annotations

import json
from pathlib import Path

from fastapi import APIRouter, HTTPException

from apex_governance.config import CONFIG_PATH, load_config
from apex_governance.models import LoginRequest, LoginResponse
from apex_governance.security import create_token

router = APIRouter()

USERS_PATH = Path(CONFIG_PATH.parent / "users.json")
DEFAULT_USERS = [{"email": "admin@apex.local", "password": "admin", "role": "admin"}]


def _load_users() -> list[dict]:
    if USERS_PATH.exists():
        try:
            return json.loads(USERS_PATH.read_text())
        except json.JSONDecodeError:
            return DEFAULT_USERS
    USERS_PATH.write_text(json.dumps(DEFAULT_USERS, indent=2))
    return DEFAULT_USERS


@router.post("/login", response_model=LoginResponse)
async def login(req: LoginRequest) -> LoginResponse:
    users = _load_users()
    if not any(u["email"] == req.email for u in users):
        raise HTTPException(status_code=401, detail="Invalid user")
    token = create_token(req.email)
    return LoginResponse(token=token, email=req.email)


@router.get("/config")
async def auth_config() -> dict:
    cfg = load_config()
    return cfg.dict()
