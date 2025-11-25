"""Routes for memory ingestion, search, and supermemory management."""

from fastapi import APIRouter, Depends, HTTPException

from apex_intelligence.core.memory_store import MemoryStore
from apex_intelligence.models import (
    IngestRequest,
    IngestResponse,
    QueryRequest,
    QueryResponse,
    MemoryAddRequest,
    MemoryListResponse,
    MemorySearchResponse,
    MemoryEntry,
)
from apex_intelligence.security import get_current_user

router = APIRouter()
store = MemoryStore()


@router.post("/ingest", response_model=IngestResponse)
async def ingest_document(req: IngestRequest, _user: str = Depends(get_current_user)) -> IngestResponse:
    doc_id = await store.ingest(req.space_id, req.content)
    return IngestResponse(doc_id=doc_id)


@router.post("/query", response_model=QueryResponse)
async def query_memory(req: QueryRequest, _user: str = Depends(get_current_user)) -> QueryResponse:
    results = await store.query(req.space_id, req.query, req.top_k)
    return QueryResponse(results=[
        MemoryEntry(id=r.id, content=r.content, space_id=r.space_id, metadata=r.metadata) if isinstance(r, MemoryEntry) else r
        for r in results
    ])


@router.post("/add", response_model=MemoryEntry)
async def add_memory(req: MemoryAddRequest, _user: str = Depends(get_current_user)) -> MemoryEntry:
    doc_id = await store.ingest(req.space_id, req.content, req.metadata)
    return MemoryEntry(id=doc_id, content=req.content, space_id=req.space_id, metadata=req.metadata)


@router.get("/list", response_model=MemoryListResponse)
async def list_memory(space_id: str | None = None, _user: str = Depends(get_current_user)) -> MemoryListResponse:
    items = await store.list(space_id)
    return MemoryListResponse(items=items)


@router.get("/search", response_model=MemorySearchResponse)
async def search_memory(q: str, space_id: str = "default", _user: str = Depends(get_current_user)) -> MemorySearchResponse:
    results = await store.query(space_id, q, 10)
    return MemorySearchResponse(query=q, results=results)


@router.delete("/{doc_id}")
async def delete_memory(doc_id: str, _user: str = Depends(get_current_user)) -> dict:
    deleted = await store.delete(doc_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Memory not found")
    return {"status": "deleted", "id": doc_id}
