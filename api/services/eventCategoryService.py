from typing import List

from api.models import EventCategory, db
from api.core import logger

EventCategories = List[EventCategory]


def getAll() -> EventCategories:
    return EventCategory.query.all()


def deleteId(id_event_category: int) -> None:
    EventCategory.query.filter(EventCategory.id == id_event_category).delete()
    db.session.commit()


def create(fields: dict) -> EventCategory:
    new_event_category = EventCategory(**fields)
    db.session.add(new_event_category)
    db.session.commit()
    return new_event_category


def getOne(event_category_id: int) -> EventCategory:
    return EventCategory.query.get(event_category_id)
