"""Python SDK for the integration service."""

from __future__ import annotations

from typing import Any, Dict
from .client import APEXClient


class IntegrationAPI:
    def __init__(self, client: APEXClient) -> None:
        self._client = client

    async def execute(self, connector_type: str, operation: str, payload: Dict[str, Any]) -> Any:
        req = {
            "connector_type": connector_type,
            "operation": operation,
            "payload": payload,
        }
        res = await self._client.post(self._client.integration_url, "/connectors/execute", req)
        res.raise_for_status()
        return res.json().get("result")