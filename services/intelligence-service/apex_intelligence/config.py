"""Runtime configuration loader for the intelligence service.

The service reads configuration from a JSON file mounted at CONFIG_PATH. The
file is re-read on every access to support auto-reload across microservices.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel, Field

DEFAULT_CONFIG: Dict[str, Any] = {
    "OPENAI_API_KEY": "",  # populated by operator
    "MODEL_NAME": "gpt-4o-mini",
    "TEMPERATURE": 0.2,
    "MAX_RETRIES": 2,
}


class RuntimeConfig(BaseModel):
    """Pydantic model describing runtime configuration."""

    OPENAI_API_KEY: str = Field(default="")
    MODEL_NAME: str = Field(default="gpt-4o-mini")
    TEMPERATURE: float = Field(default=0.2)
    MAX_RETRIES: int = Field(default=2)


CONFIG_PATH = Path(os.getenv("CONFIG_PATH", "/data/config.json"))


def _ensure_config_file() -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG, indent=2))


def load_config() -> RuntimeConfig:
    """Load runtime configuration from disk and return a RuntimeConfig object."""
    _ensure_config_file()
    try:
        data = json.loads(CONFIG_PATH.read_text())
    except json.JSONDecodeError:
        data = DEFAULT_CONFIG
    merged = {**DEFAULT_CONFIG, **data}
    return RuntimeConfig(**merged)


def update_config(payload: Dict[str, Any]) -> RuntimeConfig:
    """Persist updated configuration to disk."""
    _ensure_config_file()
    existing = load_config().dict()
    existing.update({k: v for k, v in payload.items() if k in DEFAULT_CONFIG})
    CONFIG_PATH.write_text(json.dumps(existing, indent=2))
    return RuntimeConfig(**existing)


settings = load_config()
