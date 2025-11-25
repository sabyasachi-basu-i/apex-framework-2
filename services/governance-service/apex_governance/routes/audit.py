"""Audit logging routes."""

from fastapi import APIRouter
from apex_governance.models import AuditEvent

router = APIRouter()

_audit_log: list[AuditEvent] = []


@router.post("/log")
async def log_event(event: AuditEvent) -> dict:
    """Store an audit event in memory.  Replace with persistent storage or
    external logging in production."""
    _audit_log.append(event)
    return {"logged": True}


@router.get("/events")
async def list_events() -> dict:
    """Return all logged audit events."""
    return {"events": [e.dict() for e in _audit_log]}