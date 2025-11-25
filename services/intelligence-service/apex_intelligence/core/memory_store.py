"""Simple in‑memory memory store.

This memory store holds documents in a dictionary keyed by space ID.  Each
document has an ID and content.  Queries perform a naive similarity search
using Jaccard similarity between sets of lowercase tokens.

For production use, consider integrating with a real vector database such
as Chroma, Pinecone, Weaviate or a graph database.
"""

from __future__ import annotations

import uuid
import re
from typing import Dict, List, Tuple

from apex_intelligence.models import QueryResult


class MemoryStore:
    """A simple in‑memory store mapping space IDs to lists of documents."""

    def __init__(self) -> None:
        # maps space_id -> list of (doc_id, content)
        self._spaces: Dict[str, List[Tuple[str, str]]] = {}

    async def ingest(self, space_id: str, content: str) -> str:
        """Insert a document into a space and return its generated ID."""
        docs = self._spaces.setdefault(space_id, [])
        doc_id = str(uuid.uuid4())
        docs.append((doc_id, content))
        return doc_id

    async def query(self, space_id: str, query: str, top_k: int = 5) -> List[QueryResult]:
        """Return top_k documents most similar to the query.

        Similarity is measured by Jaccard similarity of token sets.  Raises
        ValueError if the space does not exist.
        """
        if space_id not in self._spaces:
            raise ValueError(f"Space '{space_id}' not found")
        docs = self._spaces[space_id]
        if not docs:
            return []

        query_tokens = self._tokenise(query)

        scored: List[Tuple[str, float, str]] = []
        for doc_id, content in docs:
            doc_tokens = self._tokenise(content)
            score = self._jaccard(query_tokens, doc_tokens)
            scored.append((doc_id, score, content))

        # sort by descending score
        scored.sort(key=lambda x: x[1], reverse=True)
        results: List[QueryResult] = []
        for doc_id, score, content in scored[:top_k]:
            results.append(QueryResult(doc_id=doc_id, score=score, content=content))
        return results

    def _tokenise(self, text: str) -> set[str]:
        # simple whitespace and punctuation splitting, lowercasing
        tokens = re.split(r"\W+", text.lower())
        return set(filter(None, tokens))

    def _jaccard(self, a: set[str], b: set[str]) -> float:
        if not a or not b:
            return 0.0
        intersection = a & b
        union = a | b
        return len(intersection) / len(union)