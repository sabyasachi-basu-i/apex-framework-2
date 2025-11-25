"""Entry point for the integration service.

This service hosts connectors to external systems and exposes operations
to agents and flows via HTTP endpoints.
"""

from fastapi import FastAPI
from apex_integration.routes import health, connectors


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Integration Service", version="0.1.0")
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(connectors.router, prefix="/connectors", tags=["connectors"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8002)