"""Entry point for the governance service."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from apex_governance.routes import auth, rbac, audit, health
from apex_governance.routes import config as config_routes
from apex_governance.routes import graph


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Governance Service", version="0.2.0")

    @app.middleware("http")
    async def error_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:  # noqa: BLE001
            logger.exception("Unhandled error during request")
            return JSONResponse(status_code=500, content={"detail": str(exc)})

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(rbac.router, prefix="/rbac", tags=["rbac"])
    app.include_router(audit.router, prefix="/audit", tags=["audit"])
    app.include_router(config_routes.router, prefix="/config", tags=["config"])
    app.include_router(graph.router, prefix="/governance", tags=["governance"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8004)
