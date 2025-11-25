"""RBAC routes."""

from fastapi import APIRouter
from apex_governance.models import User

router = APIRouter()

# Hard-coded list of users for demonstration
_users = [
    User(email="admin@example.com", role="admin"),
    User(email="architect@example.com", role="architect"),
    User(email="developer@example.com", role="developer"),
]


@router.get("/users")
async def list_users() -> dict:
    """Return all users and their roles.  Extend with a persistent DB in the future."""
    return {"users": [user.dict() for user in _users]}