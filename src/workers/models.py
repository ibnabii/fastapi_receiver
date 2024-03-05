from datetime import datetime, timedelta
from uuid import UUID, uuid4

from beanie import Document
from pydantic import Field
import pymongo


MONGO_URI = "mongodb+srv://appUser:KiXCNj2w7hbCP68eQ3UHj3hm9HYprVQneu97H6QY@firstcluster.kyjvmkn.mongodb.net/?retryWrites=true&w=majority&appName=firstCluster"


class Worker(Document):
    id: UUID = Field(default_factory=uuid4)
    created: datetime = Field(default_factory=datetime.now)
    updated: datetime = Field(default_factory=datetime.now)
    valid_until: datetime = Field(default_factory=lambda: datetime.now() + timedelta(hours=3))

    class Settings:
        name = 'workers'
