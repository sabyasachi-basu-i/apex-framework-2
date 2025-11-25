"""Configuration for orchestration service."""

import os
from pydantic import BaseModel


class Settings(BaseModel):
    intelligence_url: str = os.getenv("INTELLIGENCE_URL", "http://localhost:8001")
    integration_url: str = os.getenv("INTEGRATION_URL", "http://localhost:8002")


settings = Settings()