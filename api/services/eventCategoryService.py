from api.models import EventCategory, db
from api.core import logger


def getAll():
    return EventCategory.query.all()


def deleteId(id_event_category: int):
    EventCategory.query.filter(EventCategory.id == id_event_category).delete()
    db.session.commit()


def create(fields):
    new_event_category = EventCategory(**fields)
    db.session.add(new_event_category)
    db.session.commit()
    return new_event_category
