"""Embedded Chroma vector store client used by the intelligence service."""

from __future__ import annotations

import uuid
from typing import Any, Dict, List, Optional

from chromadb import PersistentClient


client = PersistentClient(path="/data/chroma")
collection = client.get_or_create_collection("apex_memory")


def add_document(content: str, space_id: str, metadata: Optional[Dict[str, Any]] = None) -> str:
    """Add a document to the collection and return its identifier."""

    doc_id = str(uuid.uuid4())
    stored_metadata: Dict[str, Any] = {"space_id": space_id}
    if metadata:
        stored_metadata.update(metadata)
    collection.add(ids=[doc_id], documents=[content], metadatas=[stored_metadata])
    return doc_id


def delete_document(doc_id: str) -> bool:
    """Delete a document by ID, returning whether it existed."""

    existing = collection.get(ids=[doc_id])
    if not existing.get("ids") or not existing["ids"][0]:
        return False
    collection.delete(ids=[doc_id])
    return True


def list_documents(space_id: str | None = None) -> List[Dict[str, Any]]:
    """List documents, optionally filtering by space ID."""

    where = {"space_id": space_id} if space_id else None
    results = collection.get(where=where)
    documents = results.get("documents", [])
    ids = results.get("ids", [])
    metadatas = results.get("metadatas", [])
    return [
        {
            "id": doc_id,
            "content": doc,
            "metadata": metadata,
            "space_id": (metadata or {}).get("space_id", space_id or "default"),
        }
        for doc_id, doc, metadata in zip(ids, documents, metadatas)
    ]


def query_documents(space_id: str, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
    """Query documents for a given space using vector similarity."""

    where = {"space_id": space_id} if space_id else None
    results = collection.query(query_texts=[query], n_results=top_k, where=where)
    ids = (results.get("ids") or [[]])[0]
    documents = (results.get("documents") or [[]])[0]
    metadatas = (results.get("metadatas") or [[]])[0]
    distances = (results.get("distances") or [[]])[0]

    return [
        {
            "id": doc_id,
            "content": doc,
            "metadata": metadata,
            "space_id": (metadata or {}).get("space_id", space_id or "default"),
            "score": distance,
        }
        for doc_id, doc, metadata, distance in zip(ids, documents, metadatas, distances)
    ]
