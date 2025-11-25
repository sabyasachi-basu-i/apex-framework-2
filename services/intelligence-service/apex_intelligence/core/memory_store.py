"""Simple in-memory memory store with search capabilities."""
from __future__ import annotations

import re
import uuid
from typing import Dict, List, Tuple

from apex_intelligence.models import MemoryEntry


class MemoryStore:
    """A simple in-memory store mapping space IDs to lists of documents."""

    def __init__(self) -> None:
        self._spaces: Dict[str, List[Tuple[str, str, dict | None]]] = {}

    async def ingest(self, space_id: str, content: str, metadata: dict | None = None) -> str:
        docs = self._spaces.setdefault(space_id, [])
        doc_id = str(uuid.uuid4())
        docs.append((doc_id, content, metadata))
        return doc_id

    async def delete(self, doc_id: str) -> bool:
        for space_id, docs in self._spaces.items():
            for idx, (existing_id, _, _) in enumerate(docs):
                if existing_id == doc_id:
                    docs.pop(idx)
                    return True
        return False

    async def list(self, space_id: str | None = None) -> List[MemoryEntry]:
        entries: List[MemoryEntry] = []
        for current_space, docs in self._spaces.items():
            if space_id and current_space != space_id:
                continue
            for doc_id, content, metadata in docs:
                entries.append(MemoryEntry(id=doc_id, content=content, space_id=current_space, metadata=metadata))
        return entries

    async def query(self, space_id: str, query: str, top_k: int = 5) -> List[MemoryEntry]:
        if space_id not in self._spaces:
            return []
        docs = self._spaces[space_id]
        query_tokens = self._tokenise(query)
        scored: List[Tuple[str, float, str, dict | None]] = []
        for doc_id, content, metadata in docs:
            doc_tokens = self._tokenise(content)
            score = self._jaccard(query_tokens, doc_tokens)
            scored.append((doc_id, score, content, metadata))
        scored.sort(key=lambda x: x[1], reverse=True)
        return [MemoryEntry(id=doc_id, content=content, space_id=space_id, metadata=metadata) for doc_id, _, content, metadata in scored[:top_k]]

    def _tokenise(self, text: str) -> set[str]:
        tokens = re.split(r"\W+", text.lower())
        return set(filter(None, tokens))

    def _jaccard(self, a: set[str], b: set[str]) -> float:
        if not a or not b:
            return 0.0
        intersection = a & b
        union = a | b
        return len(intersection) / len(union)
