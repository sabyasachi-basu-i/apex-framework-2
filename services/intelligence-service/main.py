"""Entry point for the intelligence service."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger

from apex_intelligence.routes import health, memory, llm, config


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Intelligence Service", version="0.2.0")

    @app.middleware("http")
    async def error_handler(request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as exc:  # noqa: BLE001
            logger.exception("Unhandled error during request")
            return JSONResponse(status_code=500, content={"detail": str(exc)})

    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(memory.router, prefix="/memory", tags=["memory"])
    app.include_router(llm.router, prefix="/llm", tags=["llm"])
    app.include_router(config.router, prefix="/config", tags=["config"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
