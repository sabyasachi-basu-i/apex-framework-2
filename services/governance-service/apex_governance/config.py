"""Configuration for the governance service."""

import os
from pydantic import BaseModel


class Settings(BaseModel):
    secret_key: str = os.getenv("APEX_SECRET_KEY", "dev-secret")


settings = Settings()