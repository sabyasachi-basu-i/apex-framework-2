"""Configuration for the intelligence service.

Reads environment variables and exposes them via a Pydantic settings object.
"""

import os
from pydantic import BaseModel


class Settings(BaseModel):
    # environment: dev, test, prod
    environment: str = os.getenv("APEX_ENV", "local")
    # placeholder for future memory store configuration
    memory_backend: str = os.getenv("APEX_MEMORY_BACKEND", "memory")


settings = Settings()