from api.models import EventCategory, db


def getAll():
    return EventCategory.query.all()


def deleteId(id_event_category: int):
    EventCategory.query.filter(EventCategory.id == id_event_category).delete()
    db.session.commit()
