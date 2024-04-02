from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

def test_insert_event():
    event = {
        "uuid": "meu-uuid-test",
        "title": "meu title",
        "slug": "meu slug test 1",
        "maximum_attendees": 20
    }
    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)
    
def test_get_event():
    event_id = "meu-uuid-test"
    events_repository = EventsRepository()
    response = events_repository.get_eventy_by_id(event_id)
    print(response)
    