from typing import Annotated

from fastapi import Security
from fastapi.security import APIKeyHeader, HTTPBasic, HTTPBasicCredentials

from src.config import api_keys, user_credentials
from src.exceptions import UnauthorizedException


api_key_header = APIKeyHeader(name="X-Api-Key")


def check_api_key(key: str = Security(api_key_header)):
    if key not in api_keys:
        raise UnauthorizedException


basic_security = HTTPBasic()

# original from FastAPI docs
# def check_username(credentials: Annotated[HTTPBasicCredentials, Depends(basic_security)]):


def check_username(credentials: HTTPBasicCredentials = Security(basic_security)):
    for user_credential in user_credentials:
        if (
            credentials.username == user_credential.username
            and credentials.password == user_credential.password
        ):
            return
    raise UnauthorizedException
