import logging

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.config import DB_NAME, MONGO_URI


async def db_init():
    # Create Motor client
    client = AsyncIOMotorClient(MONGO_URI)
    database = client[DB_NAME]

    # Send a ping to confirm a successful connection
    logger = logging.getLogger("uvicorn")
    try:
        client.admin.command("ping")
        logger.info("Pinged! You successfully connected to MongoDB!")
    except Exception as e:
        logger.error(e)

    # Initialize beanie
    await init_beanie(
        database=database,
        document_models=[
            "src.workers.models.Worker",
            "src.submissions.models.Submission",
        ],
    )
