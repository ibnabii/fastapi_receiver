from datetime import datetime, timedelta

from pydantic import Field

from src.models import BaseDocument


class Worker(BaseDocument):
    name: str = Field(max_length=100)
    version: str = Field(max_length=100)
    pid: int | None = None
    updated: datetime = Field(default_factory=datetime.now)
    valid_until: datetime = Field(
        default_factory=lambda: datetime.now() + timedelta(hours=3)
    )

    class Config:
        json_schema_extra = {"name": "OLX crawler", "version": "0.1", "pid": 32356}

    class Settings:
        name = "workers"
        use_revision = True
