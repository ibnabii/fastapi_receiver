from datetime import datetime, timedelta
from uuid import UUID

from fastapi import Depends

from src.workers.exceptions import WorkerNotFound, WorkerExpired
from src.workers.models import Worker


async def valid_worker_id(worker_id: UUID) -> Worker:
    worker = await Worker.get(worker_id)
    if not worker:
        raise WorkerNotFound
    if worker.valid_until < datetime.now():
        raise WorkerExpired
    return worker


async def touch_worker(worker: Worker = Depends(valid_worker_id)) -> Worker:
    worker.updated = datetime.now()
    worker.valid_until = datetime.now() + timedelta(hours=3)
    await worker.save()
    return worker
