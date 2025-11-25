"""Expose API routers for the governance service."""

from . import health, auth, rbac, audit, config, graph  # noqa: F401

__all__ = ["health", "auth", "rbac", "audit", "config", "graph"]
