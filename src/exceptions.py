from fastapi import HTTPException, status


class MyHTTPException(HTTPException):
    status_code: int
    detail: str | None = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UnauthorizedException(MyHTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid or missing authentication"
