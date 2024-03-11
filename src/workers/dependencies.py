from uuid import UUID

from src.workers.exceptions import WorkerNotFound
from src.workers.models import Worker


async def valid_worker_id(worker_id: UUID) -> Worker | Exception:
    worker = await Worker.get(worker_id)
    if not worker:
        raise WorkerNotFound()
    return worker
