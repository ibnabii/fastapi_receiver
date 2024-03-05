import asyncio
import logging

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://appUser:KiXCNj2w7hbCP68eQ3UHj3hm9HYprVQneu97H6QY@firstcluster.kyjvmkn.mongodb.net/?retryWrites=true&w=majority&appName=firstCluster"
DB_NAME = "beanie_poc_db"

# Create Motor client
client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]


async def init():
    # Send a ping to confirm a successful connection
    logger = logging.getLogger("uvicorn")
    try:
        client.admin.command('ping')
        logger.info("Pinged! You successfully connected to MongoDB!")
    except Exception as e:
        logger.error(e)

    # Initialize beanie with the Sample document class and a database
    await init_beanie(
        database=database,
        document_models=[
            "workers.models.Worker",
        ]
    )

