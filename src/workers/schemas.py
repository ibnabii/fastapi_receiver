from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


class BaseWorker(BaseModel):
    name: str = Field(max_length=100)
    version: str = Field(max_length=100)
    pid: int | None = None

    model_config = {"from_attributes": True}


class WorkerCreate(BaseWorker):
    pass


class WorkerRead(BaseWorker):
    id: UUID
    created: datetime
    updated: datetime
    valid_until: datetime
    # revision_id: UUID | None = Field(None)


class WorkerCreatedResponse(BaseModel):
    id: UUID
