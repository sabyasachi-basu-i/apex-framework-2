"""Entry point for the orchestration service."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from apex_orchestration.routes import health, flows, agents, runs
from apex_orchestration.routes import config as config_routes
from apex_orchestration.routes import chat


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Orchestration Service", version="0.2.0")

    @app.middleware("http")
    async def error_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:  # noqa: BLE001
            logger.exception("Unhandled error during request")
            return JSONResponse(status_code=500, content={"detail": str(exc)})

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(flows.router, prefix="/flows", tags=["flows"])
    app.include_router(agents.router, prefix="/agents", tags=["agents"])
    app.include_router(runs.router, prefix="/runs", tags=["runs"])
    app.include_router(config_routes.router, prefix="/config", tags=["config"])
    app.include_router(chat.router, prefix="/orchestration", tags=["chat"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8003)
