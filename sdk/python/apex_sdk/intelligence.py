"""Python SDK for the intelligence service."""

from __future__ import annotations

from typing import Any, Dict, List
from .client import APEXClient


class IntelligenceAPI:
    def __init__(self, client: APEXClient) -> None:
        self._client = client

    async def ingest(self, space_id: str, content: str) -> str:
        """Ingest a document into a memory space.

        Returns the document ID.
        """
        payload = {"space_id": space_id, "content": content}
        res = await self._client.post(self._client.intelligence_url, "/memory/ingest", payload)
        res.raise_for_status()
        return res.json()["doc_id"]

    async def query(self, space_id: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        payload = {"space_id": space_id, "query": query, "top_k": top_k}
        res = await self._client.post(self._client.intelligence_url, "/memory/query", payload)
        res.raise_for_status()
        return res.json()["results"]

    async def completion(self, prompt: str, max_tokens: int = 256) -> str:
        payload = {"prompt": prompt, "max_tokens": max_tokens}
        res = await self._client.post(self._client.intelligence_url, "/llm/completions", payload)
        res.raise_for_status()
        return res.json().get("completion") or res.json().get("completion", "")