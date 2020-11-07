from api.models import Event, db


def getAll():
    return Event.query.all()


def deleteId(id_event: int):
    Event.query.filter(Event.id == id_event).delete()
    db.session.commit()


def create(fields):
    new_event = Event(**fields)
    db.session.add(new_event)
    db.session.commit()
    return new_event


def getOne(event_id: int):
    return Event.query.get(event_id)
