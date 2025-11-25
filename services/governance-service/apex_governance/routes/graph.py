"""Governance graph endpoints for flows, lineage, and agents."""
from fastapi import APIRouter, Depends

from apex_governance.security import get_current_user

router = APIRouter()


def _mock_graph(name: str) -> dict:
    return {
        "name": name,
        "nodes": [
            {"id": "start", "label": "Start"},
            {"id": "agent", "label": "Agent"},
            {"id": "end", "label": "End"},
        ],
        "edges": [
            {"source": "start", "target": "agent"},
            {"source": "agent", "target": "end"},
        ],
    }


@router.get("/flows")
async def get_flows(_user: str = Depends(get_current_user)) -> dict:
    return _mock_graph("flows")


@router.get("/lineage")
async def get_lineage(_user: str = Depends(get_current_user)) -> dict:
    return _mock_graph("lineage")


@router.get("/agents")
async def get_agents(_user: str = Depends(get_current_user)) -> dict:
    return {
        "agents": [
            {"id": "agent-1", "name": "Planner", "children": ["connector-1", "llm-1"]},
            {"id": "agent-2", "name": "Executor", "children": []},
        ]
    }
