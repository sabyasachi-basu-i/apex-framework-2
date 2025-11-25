"""Connector registry.

Connectors are registered here so that the REST API can look them up by
string identifier.  To add a new connector, import it and add an entry to
CONNECTOR_TYPES mapping.
"""

from typing import Dict, Type
from apex_integration.connectors.base import BaseConnector
from apex_integration.connectors.sql import SQLConnector
from apex_integration.connectors.salesforce import SalesforceConnector
from apex_integration.connectors.icertis import IcertisConnector
from apex_integration.connectors.blob_storage import BlobStorageConnector


CONNECTOR_TYPES: Dict[str, Type[BaseConnector]] = {
    "sql": SQLConnector,
    "salesforce": SalesforceConnector,
    "icertis": IcertisConnector,
    "blob_storage": BlobStorageConnector,
}

__all__ = ["CONNECTOR_TYPES", "BaseConnector"]