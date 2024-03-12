from uuid import UUID

from src.submissions.models import Submission


async def max_submission_no(worker_id: UUID) -> int:
    max_submission = await Submission.find({"worker_id": worker_id}).max('submission_no')

    return 0 if not max_submission else int(max_submission)
