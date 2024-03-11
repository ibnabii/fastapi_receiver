from fastapi import status

from src.exceptions import MyHTTPException


class WorkerNotFound(MyHTTPException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Worker not found"
