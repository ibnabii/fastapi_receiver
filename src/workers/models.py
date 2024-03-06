from datetime import datetime, timedelta
from typing import Any
from uuid import UUID, uuid4

from beanie import Document
from fastapi.encoders import jsonable_encoder
from pydantic import Field, model_validator


class Worker(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(max_length=100)
    version: str = Field(max_length=100)
    pid: int | None = None
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
    valid_until: datetime = Field(default_factory=lambda: datetime.now() + timedelta(hours=3))

    class Config:
        json_schema_extra = {
            "name": "OLX crawler",
            "version": "0.1",
            "pid": 32356
        }

    class Settings:
        name = 'workers'

    @model_validator(mode="before")
    @classmethod
    def set_null_microseconds(cls, data: dict[str, Any]) -> dict[str, Any]:
        datetime_fields = {
            k: v.replace(microsecond=0)
            for k, v in data.items()
            if isinstance(v, datetime)
        }

        return {**data, **datetime_fields}

    def serializable_dict(self, **kwargs):
        """Return a dict, which contains only serializable fields."""
        default_dict = self.model_dump()

        return jsonable_encoder(default_dict)
