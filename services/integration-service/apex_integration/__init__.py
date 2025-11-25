"""APEX Integration package.

Defines connectors for external systems and exposes them through FastAPI
routes.  To add a new connector, create a subclass of
`apex_integration.connectors.base.BaseConnector` and register it in
`CONNECTOR_TYPES`.
"""

from .config import settings  # noqa: F401
from .connectors import CONNECTOR_TYPES  # noqa: F401