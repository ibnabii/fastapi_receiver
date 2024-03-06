from typing import List

from fastapi import APIRouter

from src.workers.models import Worker

router = APIRouter()


@router.get("/", description="All workers, for admin only")
async def get_all_workers() -> List[Worker]:
    return await Worker.find_all().to_list()


@router.post("/", description="Create a new Worker", status_code=201)
async def create_worker(worker: Worker) -> dict:
    new_worker = await Worker.create(worker)
    return {"id": new_worker.id}
