"""Pydantic models for governance service."""

from typing import Optional
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., description="User email for login")


class LoginResponse(BaseModel):
    token: str
    email: str


class AuditEvent(BaseModel):
    user_email: Optional[str] = None
    action: str
    payload: str
    status: str


class User(BaseModel):
    email: str
    role: str