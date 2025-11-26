"""Lightweight JWT helpers for FastAPI dependencies."""
from __future__ import annotations

import os
from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import Depends, Header, HTTPException, Request, status

JWT_SECRET = os.getenv("JWT_SECRET", "change-me")
JWT_ALGORITHM = "HS256"


def create_token(sub: str, expires_minutes: int = 60) -> str:
    payload = {"sub": sub, "exp": datetime.utcnow() + timedelta(minutes=expires_minutes)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


def verify_token(request: Request, authorization: Optional[str] = Header(default=None)) -> str:
    token = None

    # Try to get token from Authorization header first
    if authorization:
        try:
            scheme, token = authorization.split(" ", 1)
            if scheme.lower() != "bearer":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth scheme")
        except ValueError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Authorization header format")

    # Fallback to cookie-based token
    if not token:
        token = request.cookies.get("_zitok") or request.cookies.get("apex-token")

    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing authentication token")

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    return payload.get("sub", "user")


def get_current_user(sub: str = Depends(verify_token)) -> str:
    return sub
