from typing import List

from fastapi import APIRouter, status

from src.workers.models import Worker
from src.workers.schemas import WorkerCreate, WorkerRead, WorkerCreatedResponse

router = APIRouter()


@router.get(
    "/", description="All workers, for admin only", response_model=list[WorkerRead]
)
async def get_all_workers() -> List[WorkerRead]:
    workers = await Worker.find_all().to_list()
    return [WorkerRead.from_orm(worker) for worker in workers]


@router.post(
    "/",
    description="Create a new Worker",
    status_code=status.HTTP_201_CREATED,
    response_model=WorkerCreatedResponse,
)
async def create_worker(worker: WorkerCreate) -> dict:
    new_worker = await Worker.create(Worker(**worker.dict()))
    return {"id": new_worker.id}
