from uuid import UUID

from pydantic import Field

from src.models import BaseDocument
from src.workers.models import Worker


class Submission(BaseDocument):
    worker_id: UUID
    submission_no: int = Field(default_factory=int)
    data: dict
