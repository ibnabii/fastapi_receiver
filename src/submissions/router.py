from typing import List

from fastapi import APIRouter, status, Depends

from src.submissions.models import Submission
from src.submissions.schemas import SubmissionCreate, SubmissionRead
from src.workers.dependencies import touch_worker
from src.workers.models import Worker

router = APIRouter()


@router.get(
    "/",
    description="All submissions, for admin only",
    response_model=list[SubmissionRead],
)
async def get_all_submissions() -> List[SubmissionRead]:
    submissions = await Submission.find_all().to_list()
    return [SubmissionRead.model_validate(submission) for submission in submissions]


@router.post(
    "/{worker_id}",
    description="Create a new Submission",
    status_code=status.HTTP_201_CREATED,
    response_model=SubmissionRead,
)
async def create_submission(submission: SubmissionCreate, worker: Worker = Depends(touch_worker)) -> SubmissionRead:
    new_submission = await Submission.create(Submission(**submission.dict(), worker_id=worker.id))
    return SubmissionRead.model_validate(new_submission)
