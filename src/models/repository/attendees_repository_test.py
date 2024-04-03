from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    attendee = {
        "uuid": "meu-uuid-test-3",
        "name": "Marcus",
        "email": "meuemail@email.com",
        "event_id": "2meu-uuid-test"
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendee)
    print(response)
    
def test_get_attendee_badge_by_id():
    id_attendee = "meu-uuid-test"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(id_attendee)
    print(response)