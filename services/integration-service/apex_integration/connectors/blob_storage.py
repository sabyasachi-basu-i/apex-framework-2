"""Placeholder blob storage connector.

This connector would be used to upload, download and list files in a
storage system such as Azure Blob Storage, AWS S3 or Google Cloud Storage.
Implement the necessary SDK calls in the methods below.
"""

from typing import Any, Dict
from apex_integration.connectors.base import BaseConnector


class BlobStorageConnector(BaseConnector):
    async def test_connection(self) -> bool:
        return False

    async def execute(self, operation: str, payload: Dict[str, Any]) -> Any:
        raise NotImplementedError("Blob storage connector is not implemented")