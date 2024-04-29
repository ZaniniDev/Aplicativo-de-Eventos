import pytest
from src.http_types.http_request import HttpRequest
from src.models.settings.connection import db_connection_handler
from .event_handler import EventHandler

db_connection_handler.connect_to_db()

# @pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-e-nois2",
        "title": "meu title",
        "slug": "meu-slug-aqui!2",
        "maximum_attendees": 20,
        "start_date": "27/04/2024 14:00",
        "finish_date": "27/04/2024 17:00",
        "address": "Rua Tuyuti, 34",
        "city": "Santos",
        "district": "Centro",
        "user_id": "1001"
    }
    http_request = HttpRequest(body=event)
    event_handler = EventHandler()
    response = event_handler.register(http_request)
    print(response)