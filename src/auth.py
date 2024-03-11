from fastapi import Security
from fastapi.security import APIKeyHeader

from src.config import api_keys
from src.exceptions import UnauthorizedException


api_key_header = APIKeyHeader(name="X-Api-Key")


def check_api_key(key: str = Security(api_key_header)):
    if key not in api_keys:
        raise UnauthorizedException
