"""Configuration for the integration service."""

import os
from pydantic import BaseModel


class Settings(BaseModel):
    sql_connection_string: str | None = os.getenv("APEX_SQL_CONNECTION_STRING")


settings = Settings()