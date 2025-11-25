"""Orchestration engine for executing flows.

The FlowEngine loads YAML flow definitions and runs each step in order.  It
delegates execution of operations to the integration and intelligence
services using asynchronous HTTP calls via httpx.
"""

from __future__ import annotations

import yaml
import httpx
from typing import Any, Dict, List, Optional
from pathlib import Path

from apex_orchestration.config import settings


class FlowExecutionError(Exception):
    """Raised when a flow fails during execution."""


class FlowEngine:
    def __init__(self, intelligence_url: Optional[str] = None, integration_url: Optional[str] = None) -> None:
        self.intelligence_url = intelligence_url or settings.intelligence_url
        self.integration_url = integration_url or settings.integration_url

    async def run_flow(self, flow_def: Dict[str, Any], inputs: Dict[str, Any] | None = None) -> Dict[str, Any]:
        """Execute a flow and return its execution context.

        Parameters
        ----------
        flow_def: dict
            Parsed YAML representing the flow
        inputs: dict
            Optional inputs (unused for now)

        Returns
        -------
        dict
            Execution context containing results for each step
        """
        ctx: Dict[str, Any] = {"inputs": inputs or {}}
        steps: List[Dict[str, Any]] = flow_def.get("steps", [])
        async with httpx.AsyncClient() as client:
            for step in steps:
                step_id = step.get("id") or f"step_{len(ctx)}"
                step_type = step.get("type")
                if step_type == "connector_call":
                    result = await self._execute_connector_step(client, step)
                elif step_type == "llm_call":
                    result = await self._execute_llm_step(client, step)
                elif step_type == "api_call":
                    result = await self._execute_api_step(client, step)
                else:
                    # unknown step type; store error
                    result = {"error": f"Unknown step type '{step_type}'"}
                ctx[step_id] = result
        return ctx

    async def _execute_connector_step(self, client: httpx.AsyncClient, step: Dict[str, Any]) -> Any:
        payload = {
            "connector_type": step.get("connector"),
            "operation": step.get("operation"),
            "payload": step.get("payload", {}),
        }
        url = f"{self.integration_url}/connectors/execute"
        response = await client.post(url, json=payload, timeout=60.0)
        response.raise_for_status()
        return response.json().get("result")

    async def _execute_llm_step(self, client: httpx.AsyncClient, step: Dict[str, Any]) -> Any:
        # For now support memory query or completions via explicit fields
        if "space_id" in step:
            # call memory query
            query_payload = {
                "space_id": step["space_id"],
                "query": step.get("prompt"),
                "top_k": step.get("top_k", 5),
            }
            url = f"{self.intelligence_url}/memory/query"
            response = await client.post(url, json=query_payload, timeout=60.0)
            response.raise_for_status()
            return response.json().get("results")
        elif step.get("endpoint") == "completions":
            comp_payload = {
                "prompt": step.get("prompt"),
                "max_tokens": step.get("max_tokens", 256),
            }
            url = f"{self.intelligence_url}/llm/completions"
            response = await client.post(url, json=comp_payload, timeout=60.0)
            response.raise_for_status()
            return response.json()
        else:
            return {"error": "Invalid llm_call step; specify space_id or endpoint"}

    async def _execute_api_step(self, client: httpx.AsyncClient, step: Dict[str, Any]) -> Any:
        # Generic HTTP call to an external API; expects method, url and payload
        method = step.get("method", "get").lower()
        url = step.get("url")
        payload = step.get("payload", {})
        if not url:
            return {"error": "Missing url for api_call"}
        request_func = getattr(client, method)
        response = await request_func(url, json=payload, timeout=60.0)
        try:
            response.raise_for_status()
            # return JSON if possible, else text
            try:
                return response.json()
            except Exception:
                return response.text
        except Exception as err:
            return {"error": str(err), "status_code": response.status_code}

    @staticmethod
    def load_flow_from_file(path: str) -> Dict[str, Any]:
        """Load a flow from a YAML file relative to the repository root."""
        resolved = Path(path)
        if not resolved.exists():
            raise FileNotFoundError(f"Flow file '{path}' does not exist")
        with resolved.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f)