from typing import List

from api.core import logger
from api.models import Event, db
from api.services import eventCategoryService

Events = List[Event]


def getAll() -> Events:
    return Event.query.all()


def deleteId(id_event: int) -> None:
    getOne(id_event).event_categories = []
    Event.query.filter(Event.id == id_event).delete()
    db.session.commit()


def create(fields: dict) -> Event:
    event_categories_ids = fields.get("event_categories_ids", [])
    fields.pop('event_categories_ids', None)
    event_categories = eventCategoryService.getAllIds(event_categories_ids)
    if event_categories:
        fields["event_categories"] = event_categories
    new_event = Event(**fields)
    db.session.add(new_event)
    db.session.commit()
    return new_event


def getOne(event_id: int) -> Event or None:
    return Event.query.get(event_id)


def update(event_id: int, fields: dict) -> Event or None:
    event = getOne(event_id)
    if not event:
        return None
    event.start_date = fields["start_date"]
    event.end_date = fields["end_date"]
    event.title = fields["title"]
    event.place = fields["place"]
    event.description = fields["description"]

    # Let's update categories
    if "event_categories_ids" in fields:
        event.event_categories = eventCategoryService.getAllIds(fields['event_categories_ids'])

    db.session.commit()
    return event


def getEventWithCategories(event_category_ids: []) -> Events:
    events = getAll()
    if not event_category_ids:
        return events
    filtered_events = []
    for event in events:
        for event_category in event.event_categories:
            if str(event_category.id) in event_category_ids:
                filtered_events.append(event)
                break
    return filtered_events
