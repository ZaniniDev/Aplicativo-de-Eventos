import uuid
from src.models.repository.users_repository import UsersRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from datetime import datetime

class UserHandler:
    def __init__(self) -> None:
        self.__users_repository = UsersRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        if "uuid" not in body:
            body["uuid"] = str(uuid.uuid4())
        
        self.__users_repository.insert_user(body)

        return HttpResponse(
            body={ "eventId": body["uuid"] },
            status_code=200
        ) 