from api.models import Person, db


def getAll():
    return Person.query.all()


def deleteId(id_person: int):
    Person.query.filter(Person.id == id_person).delete()
    db.session.commit()


def create(fields):
    fields["validate"] = True
    new_person = Person(**fields)
    db.session.add(new_person)
    db.session.commit()
    return new_person


def getOne(person_id: int):
    return Person.query.get(person_id)
