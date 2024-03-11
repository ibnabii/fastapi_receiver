from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from src.workers.models import Worker


class BaseSubmission(BaseModel):
    data: dict

    class Config:
        from_attributes = True


class SubmissionCreate(BaseSubmission):
    pass


class SubmissionRead(BaseSubmission):
    id: UUID
    worker_id: UUID
    submission_no: int
    created: datetime
