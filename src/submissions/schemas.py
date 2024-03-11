from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field

from src.workers.models import Worker


class BaseSubmission(BaseModel):
    worker_id: UUID
    data: dict

    class Config:
        from_attributes = True


class SubmissionCreate(BaseSubmission):
    pass


class SubmissionRead(BaseSubmission):
    id: UUID
    submission_no: int
    created: datetime
