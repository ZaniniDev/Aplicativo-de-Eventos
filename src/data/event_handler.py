import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.errors.error_types.http_not_found import HttpNotFoundError
from datetime import datetime

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        print(body)
        body["uuid"] = str(uuid.uuid4())
        format_datetime = "%d/%m/%Y %H:%M"    
        try:             
            body["slug"] = body["title"] + " " + body["start_date"]
            body["start_date"] = datetime.strptime(body["start_date"], format_datetime)
            body["finish_date"] = datetime.strptime(body["finish_date"], format_datetime)
        except Exception as exception:
            msg_error = str(exception)
            print(msg_error)
            return HttpResponse(
                body={"message": "A data precisa estar no formato dd/MM/yyyy hh:mm !"},
                status_code=400
            )
        
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={ "eventId": body["uuid"] },
            status_code=200
        )        

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise HttpNotFoundError("Evento não encontrado")

        event_attendees_count = self.__events_repository.count_event_attendees(event_id)

        return HttpResponse(
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "address": event.address,
                    "city": event.city,
                    "district": event.district,
                    "online": event.online,
                    "location": event.location,
                    "start_date": event.start_date,
                    "finish_date": event.finish_date,
                    "maximum_attendees": event.maximum_attendees,
                    "attendeesAmount": event_attendees_count["attendeesAmount"]
                }
            },
            status_code=200
        )
    
    def find_events_actives(self, http_request: HttpRequest) -> HttpResponse:
        events = self.__events_repository.get_events_actives()
        formatted_events = []
        for event in events:
            formatted_events.append(
                {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "address": event.address,
                    "city": event.city,
                    "district": event.district,
                    "online": event.online,
                    "location": event.location,
                    "start_date": event.start_date,
                    "finish_date": event.finish_date,
                    "maximum_attendees": event.maximum_attendees,
                }
            )

        return HttpResponse(
            body={ "events": formatted_events },
            status_code=200
        )
    
    def find_events_by_user(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.param["user_id"]
        events = self.__events_repository.get_events_by_user(user_id=user_id)
        formatted_events = []
        for event in events:
            formatted_events.append(
                {
                    "id": event.id,
                    "title": event.title,
                    "detail": event.details,
                    "slug": event.slug,
                    "address": event.address,
                    "city": event.city,
                    "district": event.district,
                    "online": event.online,
                    "location": event.location,
                    "start_date": event.start_date,
                    "finish_date": event.finish_date,
                    "maximum_attendees": event.maximum_attendees,
                }
            )

        return HttpResponse(
            body={ "events": formatted_events },
            status_code=200
        )
