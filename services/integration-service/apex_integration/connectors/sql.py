"""SQL connector using SQLAlchemy.

Supports executing read queries.  To customise the connection string,
provide it when instantiating the connector or via the payload.
"""

from __future__ import annotations

from typing import Any, Dict, List
import sqlalchemy

from apex_integration.connectors.base import BaseConnector
from apex_integration.config import settings


class SQLConnector(BaseConnector):
    """Connector for relational databases via SQLAlchemy."""

    async def test_connection(self) -> bool:
        connection_string = self.config.get("connection_string") or settings.sql_connection_string
        if not connection_string:
            # Cannot test connection without a connection string
            return False
        engine = sqlalchemy.create_engine(connection_string)
        try:
            with engine.connect() as conn:
                conn.execute(sqlalchemy.text("SELECT 1"))
            return True
        except Exception:
            return False

    async def execute(self, operation: str, payload: Dict[str, Any]) -> List[Dict[str, Any]]:
        if operation != "query":
            raise ValueError(f"Unsupported operation '{operation}' for SQL connector")
        connection_string = (
            payload.get("connection_string")
            or self.config.get("connection_string")
            or settings.sql_connection_string
        )
        if not connection_string:
            raise ValueError("No connection string provided")
        query: str = payload.get("query")
        params: Dict[str, Any] = payload.get("params", {})
        engine = sqlalchemy.create_engine(connection_string)
        with engine.connect() as conn:
            result = conn.execute(sqlalchemy.text(query), params)
            return [dict(row._mapping) for row in result]