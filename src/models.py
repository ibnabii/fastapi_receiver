from datetime import datetime
from typing import Any
from uuid import UUID, uuid4

from beanie import Document
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, model_validator


class BaseDocument(Document):
    id: UUID = Field(default_factory=uuid4)
    created: datetime = Field(default_factory=datetime.now)

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


class ErrorModel(BaseModel):
    detail: str | None

    model_config = {"json_schema_extra": {"examples": [{"detail": "Object not found"}]}}
