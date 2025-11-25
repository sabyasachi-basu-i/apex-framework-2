"""Python SDK for the governance service."""

from __future__ import annotations

from typing import Any, Dict, List
from .client import APEXClient


class GovernanceAPI:
    def __init__(self, client: APEXClient) -> None:
        self._client = client

    async def login(self, email: str) -> Dict[str, Any]:
        res = await self._client.post(self._client.governance_url, "/auth/login", {"email": email})
        res.raise_for_status()
        return res.json()

    async def list_users(self) -> List[Dict[str, Any]]:
        res = await self._client.get(self._client.governance_url, "/rbac/users")
        res.raise_for_status()
        return res.json().get("users", [])

    async def list_audit_events(self) -> List[Dict[str, Any]]:
        res = await self._client.get(self._client.governance_url, "/audit/events")
        res.raise_for_status()
        return res.json().get("events", [])