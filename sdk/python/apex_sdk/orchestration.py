"""Python SDK for the orchestration service."""

from __future__ import annotations

from typing import Any, Dict
from .client import APEXClient


class OrchestrationAPI:
    def __init__(self, client: APEXClient) -> None:
        self._client = client

    async def run_flow(self, flow_path: str, inputs: Dict[str, Any] | None = None) -> Dict[str, Any]:
        req = {
            "flow_path": flow_path,
            "inputs": inputs or {},
        }
        res = await self._client.post(self._client.orchestration_url, "/flows/run", req)
        res.raise_for_status()
        return res.json()["context"]