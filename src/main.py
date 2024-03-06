from fastapi import FastAPI

from src.database import db_init

from src.workers.router import router as worker_router

app = FastAPI(
    title="FastAPI PoC",
    description="PoC for using FastAPI with MongoDB (via Beanie)"
)


@app.on_event("startup")
async def startup():
    await db_init()


@app.get("/ping", tags=["Healthcheck"])
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


app.include_router(worker_router, prefix="/worker", tags=["Workers"])
