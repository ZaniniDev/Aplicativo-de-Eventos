from typing import Dict, List
from src.models.settings.connection import db_connection_handler
from src.models.entities.users import Users
from src.models.entities.events import Events
from src.models.entities.attendees import Attendees
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from src.errors.error_types.http_conflict import HttpConflictError
from datetime import date, datetime

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                event = Events(
                    id=eventsInfo.get("uuid"),
                    title=eventsInfo.get("title"),
                    details=eventsInfo.get("details"),
                    slug=eventsInfo.get("slug"),
                    maximum_attendees=eventsInfo.get("maximum_attendees"),
                    start_date=eventsInfo.get("start_date"),
                    finish_date=eventsInfo.get("finish_date"),                    
                    address=eventsInfo.get("address"),
                    city=eventsInfo.get("city"),
                    district=eventsInfo.get("district"),
                    online=eventsInfo.get("online"),
                    location=eventsInfo.get("location"),
                    user_id=eventsInfo.get("user_id"),
                )
                database.session.add(event)
                database.session.commit()

                return eventsInfo
            except IntegrityError as e:
                print(event)
                print("erro aqui")
                print(e)
                raise HttpConflictError('Evento ja cadastrado!')
            except Exception as exception:
                database.session.rollback()
                print(exception)
                raise exception

    def get_event_by_id(self, event_id: str) -> Events:
        with db_connection_handler as database:
            try:
                event = (
                    database.session
                        .query(Events)
                        .filter(Events.id==event_id)
                        .one()
                )
                return event
            except NoResultFound:
                return None
            
    def get_events_actives(self) -> List[Events]:
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # Define a hora como 00:00:00
        date
        with db_connection_handler as database:
            try:
                events = (
                    database.session
                        .query(Events)
                        .filter(Events.start_date >= today)
                        .order_by(Events.start_date.asc())
                        .all()
                )
                return events
            except NoResultFound:
                return None
            
    def get_events_by_user(self, user_id: str) -> List[Events]:
        with db_connection_handler as database:
            try:
                events = (
                    database.session
                        .query(Events)
                        .filter(Events.user_id == user_id)
                        .order_by(Events.start_date.asc())
                        .all()
                )
                return events
            except NoResultFound:
                return None

    def count_event_attendees(self, event_id: str) -> Dict:
        with db_connection_handler as database:
            event_count = (
                database.session
                    .query(Events)
                    .join(Attendees, Events.id == Attendees.event_id)
                    .filter(Events.id==event_id)
                    .with_entities(
                        Events.maximum_attendees,
                        Attendees.id
                    )
                    .all()
            )
            if not len(event_count):
                return {
                    "maximum_attendees": 0,
                    "attendeesAmount": 0,
                }

            return {
                "maximum_attendees": event_count[0].maximum_attendees,
                "attendeesAmount": len(event_count),
            }
