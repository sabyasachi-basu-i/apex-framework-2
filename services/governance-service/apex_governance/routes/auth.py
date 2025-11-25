"""Authentication routes."""

import base64
from fastapi import APIRouter
from apex_governance.models import LoginRequest, LoginResponse
from apex_governance.config import settings

router = APIRouter()


@router.post("/login", response_model=LoginResponse)
async def login(req: LoginRequest) -> LoginResponse:
    """Issue a simple encoded token for the user email.

    This is a placeholder.  In production you should validate credentials
    and use a proper JWT library such as `python-jose` to sign tokens.
    """
    token_raw = f"{req.email}:{settings.secret_key}"
    token_bytes = token_raw.encode("utf-8")
    token_b64 = base64.urlsafe_b64encode(token_bytes).decode("utf-8")
    return LoginResponse(token=token_b64, email=req.email)