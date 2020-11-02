from api.models import Event, db


def getAll():
    return Event.query.all()


def deleteId(id_event: int):
    Event.query.filter(Event.id == id_event).delete()
    db.session.commit()