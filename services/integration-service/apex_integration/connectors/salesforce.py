"""Placeholder Salesforce connector.

To implement this connector, authenticate against Salesforce's REST API
and expose operations such as query, insert and update.  See the
Salesforce API documentation for details.
"""

from typing import Any, Dict
from apex_integration.connectors.base import BaseConnector


class SalesforceConnector(BaseConnector):
    async def test_connection(self) -> bool:
        # not implemented
        return False

    async def execute(self, operation: str, payload: Dict[str, Any]) -> Any:
        raise NotImplementedError("Salesforce connector is not implemented")