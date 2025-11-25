"""Entry point for the intelligence service.

This service exposes memory ingestion and querying, as well as a placeholder LLM
completion endpoint.  It is implemented using FastAPI and can be run
standalone or via Docker Compose.
"""

from fastapi import FastAPI
from apex_intelligence.routes import health, memory, llm


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="APEX Intelligence Service", version="0.1.0")
    # mount routers
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(memory.router, prefix="/memory", tags=["memory"])
    app.include_router(llm.router, prefix="/llm", tags=["llm"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)