"""Entry point for the orchestration service.

This service loads flows defined in YAML files and executes them sequentially
by delegating to the integration and intelligence services.
"""

from fastapi import FastAPI
from apex_orchestration.routes import health, flows, agents, runs


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Orchestration Service", version="0.1.0")
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(flows.router, prefix="/flows", tags=["flows"])
    app.include_router(agents.router, prefix="/agents", tags=["agents"])
    app.include_router(runs.router, prefix="/runs", tags=["runs"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)