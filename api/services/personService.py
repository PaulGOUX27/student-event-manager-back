from typing import List

from api.models import Person, db

Persons = List[Person]


def getAll() -> Persons:
    return Person.query.all()


def deleteId(id_person: int) -> None:
    Person.query.filter(Person.id == id_person).delete()
    db.session.commit()


def create(fields: dict) -> Person:
    fields["validate"] = True
    new_person = Person(**fields)
    db.session.add(new_person)
    db.session.commit()
    return new_person


def getOne(person_id: int) -> Person:
    return Person.query.get(person_id)
