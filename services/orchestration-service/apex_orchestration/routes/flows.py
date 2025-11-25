"""Flow execution routes."""

from fastapi import APIRouter, HTTPException
from apex_orchestration.models import RunFlowRequest, RunFlowResponse
from apex_orchestration.engine import FlowEngine, FlowExecutionError

router = APIRouter()
engine = FlowEngine()


@router.post("/run", response_model=RunFlowResponse)
async def run_flow(req: RunFlowRequest) -> RunFlowResponse:
    """Load a flow from disk and execute it."""
    try:
        flow_def = engine.load_flow_from_file(req.flow_path)
    except FileNotFoundError as err:
        raise HTTPException(status_code=404, detail=str(err))
    try:
        context = await engine.run_flow(flow_def, req.inputs)
        return RunFlowResponse(context=context)
    except FlowExecutionError as err:
        raise HTTPException(status_code=500, detail=str(err))