from typing import List

from api.models import Event, db

Events = List[Event]


def getAll() -> Events:
    return Event.query.all()


def deleteId(id_event: int) -> None:
    Event.query.filter(Event.id == id_event).delete()
    db.session.commit()


def create(fields: dict) -> Event:
    new_event = Event(**fields)
    db.session.add(new_event)
    db.session.commit()
    return new_event


def getOne(event_id: int) -> Event:
    return Event.query.get(event_id)
