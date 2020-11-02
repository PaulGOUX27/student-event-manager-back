from api.models import Person, db


def getAll():
    return Person.query.all()


def deleteId(id_person: int):
    Person.query.filter(Person.id == id_person).delete()
    db.session.commit()
