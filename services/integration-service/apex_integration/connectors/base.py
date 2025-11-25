"""Base class for all connectors.

A connector encapsulates the logic required to interface with an external
system.  All connectors must implement `test_connection` and `execute`.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseConnector(ABC):
    """Abstract base connector."""

    def __init__(self, config: Dict[str, Any] | None = None) -> None:
        # Each connector may accept its own configuration
        self.config = config or {}

    @abstractmethod
    async def test_connection(self) -> bool:
        """Return True if the connector can communicate with its target."""

    @abstractmethod
    async def execute(self, operation: str, payload: Dict[str, Any]) -> Any:
        """Execute an operation against the external system and return the result."""