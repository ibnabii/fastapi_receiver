from uuid import UUID

from beanie.odm.operators.group import Group

from src.submissions.models import Submission


async def max_submission_no(worker_id: UUID) -> int:
    pipeline = [
        Group(
            _id=None,
            max_submission_no={"$max": "$submission_no"}
        )
    ]

    # Execute the aggregation pipeline
    max_submission_no_result = await Submission.aggregate(pipeline).find_one(
