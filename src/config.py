from dataclasses import dataclass
from os import environ as env
from json import loads


@dataclass
class Credentials:
    username: str
    password: str


MONGO_URI = env["MONGO_URI"]
DB_NAME = env["DB_NAME"]
USER_CREDENTIALS = env["USER_CREDENTIALS"]

user_credentials = [Credentials(**cred) for cred in loads(USER_CREDENTIALS)]

api_keys = loads(env["API_KEYS"])
