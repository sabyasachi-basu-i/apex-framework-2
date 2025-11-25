"""Routes for memory ingestion and querying."""

from fastapi import APIRouter, HTTPException
from apex_intelligence.core.memory_store import MemoryStore
from apex_intelligence.models import IngestRequest, IngestResponse, QueryRequest, QueryResponse

router = APIRouter()
store = MemoryStore()


@router.post("/ingest", response_model=IngestResponse)
async def ingest_document(req: IngestRequest) -> IngestResponse:
    """Ingest a document into a memory space.  Returns a document ID."""
    doc_id = await store.ingest(req.space_id, req.content)
    return IngestResponse(doc_id=doc_id)


@router.post("/query", response_model=QueryResponse)
async def query_memory(req: QueryRequest) -> QueryResponse:
    """Query the memory space for relevant documents.  Returns top_k results with scores."""
    try:
        results = await store.query(req.space_id, req.query, req.top_k)
    except ValueError as err:
        raise HTTPException(status_code=404, detail=str(err))
    return QueryResponse(results=results)