from fastapi import FastAPI

from database import db_init

app = FastAPI(
    title="FastAPI PoC",
    description="PoC for using FastAPI with MongoDB (via Beanie)"
)


@app.on_event("startup")
async def startup():
    await db_init()



