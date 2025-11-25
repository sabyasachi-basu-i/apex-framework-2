"""HTTP endpoints for executing connector operations."""

from typing import Any, Dict

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from apex_integration.connectors import CONNECTOR_TYPES
from apex_integration.security import get_current_user

router = APIRouter()


class ExecuteRequest(BaseModel):
    connector_type: str = Field(..., description="Type of connector to use")
    operation: str = Field(..., description="Operation name, e.g. 'query'")
    payload: Dict[str, Any] = Field({}, description="Operation payload")


class ExecuteResponse(BaseModel):
    result: Any


@router.post("/execute", response_model=ExecuteResponse)
async def execute_operation(req: ExecuteRequest, _user: str = Depends(get_current_user)) -> ExecuteResponse:
    connector_cls = CONNECTOR_TYPES.get(req.connector_type)
    if not connector_cls:
        raise HTTPException(status_code=400, detail=f"Unsupported connector type '{req.connector_type}'")

    connector = connector_cls()
    try:
        result = await connector.execute(req.operation, req.payload)
    except Exception as err:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(err))
    return ExecuteResponse(result=result)
