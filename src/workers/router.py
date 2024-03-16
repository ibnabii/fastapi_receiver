from typing import List

from fastapi import APIRouter, status, Depends

from src.auth import check_api_key, check_username
from src.models import ErrorModel
from src.workers.dependencies import touch_worker
from src.workers.models import Worker
from src.workers.schemas import WorkerCreate, WorkerRead, WorkerCreatedResponse

router = APIRouter()


@router.get(
    "/",
    description="All workers, for admin only",
    response_model=list[WorkerRead],
    dependencies=(Depends(check_username),),
)
async def get_all_workers() -> List[WorkerRead]:
    workers = await Worker.find_all().to_list()
    return [WorkerRead.model_validate(worker) for worker in workers]


@router.post(
    "/",
    description="Create a new Worker",
    status_code=status.HTTP_201_CREATED,
    response_model=WorkerCreatedResponse,
    dependencies=(Depends(check_api_key),),
)
async def create_worker(worker: WorkerCreate) -> dict:
    new_worker = await Worker.create(Worker(**worker.dict()))
    return {"id": new_worker.id}


# just for poc
# @router.get(
#     "/{worker_id}",
#     response_model=WorkerRead,
#     description="Test endpoint to check updating Worker's validity",
#     responses={
#         404: {"model": ErrorModel},
#         403: {
#             "model": ErrorModel,
#             "content": {
#                 "application/json": {
#                     "examples": {
#                         "default": {
#                             "summary": "default",
#                             "value": {"detail": "Worker expired"},
#                         }
#                     }
#                 }
#             },
#         },
#     },
#     dependencies=(Depends(check_username),),
# )
# async def get_worker(worker: Worker = Depends(touch_worker)):
#     return WorkerRead.model_validate(worker)
