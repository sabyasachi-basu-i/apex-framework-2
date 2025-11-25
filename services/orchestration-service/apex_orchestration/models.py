"""Pydantic models for orchestration service."""

from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class RunFlowRequest(BaseModel):
    """Request body for running a flow."""

    flow_path: str = Field(..., description="Path to the flow YAML file")
    inputs: Optional[Dict[str, Any]] = Field(default_factory=dict)


class RunFlowResponse(BaseModel):
    """Response returned after running a flow."""

    context: Dict[str, Any]