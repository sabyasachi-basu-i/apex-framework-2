"""Core client for APEX services.

The `APEXClient` wraps an asynchronous HTTP client and exposes API
wrappers for the intelligence, integration, orchestration and governance
services.  It reads base URLs from environment variables if not
provided explicitly.
"""

from __future__ import annotations

import os
from typing import Optional
import httpx

from .intelligence import IntelligenceAPI
from .integration import IntegrationAPI
from .orchestration import OrchestrationAPI
from .governance import GovernanceAPI


class APEXClient:
    def __init__(
        self,
        intelligence_url: Optional[str] = None,
        integration_url: Optional[str] = None,
        orchestration_url: Optional[str] = None,
        governance_url: Optional[str] = None,
        timeout: float = 30.0,
    ) -> None:
        self.intelligence_url = intelligence_url or os.getenv("INTELLIGENCE_URL", "http://localhost:8001")
        self.integration_url = integration_url or os.getenv("INTEGRATION_URL", "http://localhost:8002")
        self.orchestration_url = orchestration_url or os.getenv("ORCHESTRATION_URL", "http://localhost:8003")
        self.governance_url = governance_url or os.getenv("GOVERNANCE_URL", "http://localhost:8004")
        self._client = httpx.AsyncClient(timeout=timeout)
        # attach API wrappers
        self.intelligence = IntelligenceAPI(self)
        self.integration = IntegrationAPI(self)
        self.orchestration = OrchestrationAPI(self)
        self.governance = GovernanceAPI(self)

    async def post(self, base_url: str, path: str, json: dict) -> httpx.Response:
        url = f"{base_url}{path}"
        return await self._client.post(url, json=json)

    async def get(self, base_url: str, path: str) -> httpx.Response:
        url = f"{base_url}{path}"
        return await self._client.get(url)

    async def __aenter__(self) -> "APEXClient":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self._client.aclose()

    async def close(self) -> None:
        await self._client.aclose()