"""Pydantic models used by the intelligence service."""

from typing import List
from pydantic import BaseModel, Field


class IngestRequest(BaseModel):
    """Request body for ingesting a document into memory."""

    space_id: str = Field(..., description="Name of the memory space")
    content: str = Field(..., description="Raw text content to store")


class IngestResponse(BaseModel):
    """Response returned after ingesting a document."""

    doc_id: str = Field(..., description="Identifier of the stored document")


class QueryRequest(BaseModel):
    """Request body for querying a memory space."""

    space_id: str = Field(..., description="Name of the memory space")
    query: str = Field(..., description="Query text")
    top_k: int = Field(5, description="Number of results to return")


class QueryResult(BaseModel):
    """One matching document and its relevance score."""

    doc_id: str
    score: float
    content: str


class QueryResponse(BaseModel):
    """Response returned after querying memory."""

    results: List[QueryResult]


class CompletionRequest(BaseModel):
    """Request for an LLM completion."""

    prompt: str
    max_tokens: int = 256


class CompletionResponse(BaseModel):
    """LLM completion response."""

    completion: str