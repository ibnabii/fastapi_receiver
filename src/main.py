from fastapi import FastAPI
from pydantic import BaseModel

from src.database import db_init

from src.workers.router import router as worker_router
from src.submissions.router import router as submission_router

app = FastAPI(
    title="FastAPI PoC", description="PoC for using FastAPI with MongoDB (via Beanie)"
)


@app.on_event("startup")
async def startup():
    await db_init()


class HealthCheckResponse(BaseModel):
    status: str = "ok"


@app.get("/ping", tags=["Healthcheck"], response_model=HealthCheckResponse)
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(worker_router, prefix="/workers", tags=["Workers"])
app.include_router(submission_router, prefix="/submissions", tags=["Submissions"])
