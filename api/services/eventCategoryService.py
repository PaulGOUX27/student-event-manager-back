from typing import List

from sqlalchemy import any_

from api.models import EventCategory, db
from api.core import logger

EventCategories = List[EventCategory]


def getAll() -> EventCategories:
    return EventCategory.query.all()


def getAllIds(event_category_ids=None) -> EventCategories:
    if not event_category_ids:
        return []
    # return EventCategory.query.filter(EventCategory.id.like(any_(ids)))
    event_categories = []
    for event_category_id in event_category_ids:
        event_categories.append(getOne(event_category_id))
    return event_categories


def deleteId(id_event_category: int) -> None:
    EventCategory.query.filter(EventCategory.id == id_event_category).delete()
    db.session.commit()


def create(fields: dict) -> EventCategory:
    new_event_category = EventCategory(**fields)
    db.session.add(new_event_category)
    db.session.commit()
    return new_event_category


def getOne(event_category_id: int) -> EventCategory or None:
    return EventCategory.query.get(event_category_id)


def update(event_category_id: int, fields: dict) -> EventCategory or None:
    event_category = getOne(event_category_id)
    if not event_category:
        return None
    event_category.name = fields['name']
    db.session.commit()
    return event_category
