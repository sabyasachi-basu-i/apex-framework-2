"""Chroma-backed memory store utilities."""
from __future__ import annotations

from typing import Dict, List

from apex_intelligence.models import MemoryEntry
from apex_intelligence.vector_store import add_document, delete_document, list_documents, query_documents


class MemoryStore:
    """Persistence wrapper over the embedded Chroma collection."""

    async def ingest(self, space_id: str, content: str, metadata: Dict | None = None) -> str:
        return add_document(content=content, space_id=space_id, metadata=metadata)

    async def delete(self, doc_id: str) -> bool:
        return delete_document(doc_id)

    async def list(self, space_id: str | None = None) -> List[MemoryEntry]:
        docs = list_documents(space_id)
        return [
            MemoryEntry(
                id=doc["id"],
                content=doc["content"],
                space_id=doc["space_id"],
                metadata=doc.get("metadata"),
            )
            for doc in docs
        ]

    async def query(self, space_id: str, query: str, top_k: int = 5) -> List[Dict]:
        return query_documents(space_id=space_id, query=query, top_k=top_k)
