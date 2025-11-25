"""Configuration for the governance service."""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict

from pydantic import BaseModel, Field

DEFAULT_CONFIG: Dict[str, Any] = {
    "OPENAI_API_KEY": "",
    "MODEL_NAME": "gpt-4o-mini",
    "TEMPERATURE": 0.2,
    "MAX_RETRIES": 2,
    "SECRET_KEY": os.getenv("APEX_SECRET_KEY", "dev-secret"),
}


class RuntimeConfig(BaseModel):
    OPENAI_API_KEY: str = Field(default="")
    MODEL_NAME: str = Field(default="gpt-4o-mini")
    TEMPERATURE: float = Field(default=0.2)
    MAX_RETRIES: int = Field(default=2)
    SECRET_KEY: str = Field(default="dev-secret")


CONFIG_PATH = Path(os.getenv("CONFIG_PATH", "/data/config.json"))


def _ensure_config_file() -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG, indent=2))


def load_config() -> RuntimeConfig:
    _ensure_config_file()
    try:
        data = json.loads(CONFIG_PATH.read_text())
    except json.JSONDecodeError:
        data = DEFAULT_CONFIG
    merged = {**DEFAULT_CONFIG, **data}
    return RuntimeConfig(**merged)


def update_config(payload: Dict[str, Any]) -> RuntimeConfig:
    _ensure_config_file()
    existing = load_config().dict()
    existing.update({k: v for k, v in payload.items() if k in DEFAULT_CONFIG})
    CONFIG_PATH.write_text(json.dumps(existing, indent=2))
    return RuntimeConfig(**existing)


settings = load_config()
