from typing import List

from fastapi import APIRouter, status

from src.submissions.models import Submission
from src.submissions.schemas import SubmissionCreate, SubmissionRead

router = APIRouter()


@router.get(
    "/",
    description="All submissions, for admin only",
    response_model=list[SubmissionRead],
)
async def get_all_submissions() -> List[SubmissionRead]:
    submissions = await Submission.find_all().to_list()
    return [SubmissionRead.from_orm(submission) for submission in submissions]


@router.post(
    "/",
    description="Create a new Submission",
    status_code=status.HTTP_201_CREATED,
    response_model=SubmissionRead,
)
async def create_submission(submission: SubmissionCreate) -> SubmissionRead:
    new_submission = await Submission.create(Submission(**submission.dict()))
    return SubmissionRead.from_orm(new_submission)
