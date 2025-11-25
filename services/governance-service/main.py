"""Entry point for the governance service."""

from fastapi import FastAPI
from apex_governance.routes import auth, rbac, audit, health


def create_app() -> FastAPI:
    app = FastAPI(title="APEX Governance Service", version="0.1.0")
    app.include_router(health.router, prefix="/health", tags=["health"])
    app.include_router(auth.router, prefix="/auth", tags=["auth"])
    app.include_router(rbac.router, prefix="/rbac", tags=["rbac"])
    app.include_router(audit.router, prefix="/audit", tags=["audit"])
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8004)