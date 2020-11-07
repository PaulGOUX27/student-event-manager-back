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


def getOne(person_id: int) -> Person or None:
    return Person.query.get(person_id)


def update(person_id: int, fields: dict) -> Person or None:
    person = getOne(person_id)
    if not person:
        return None
    person.login = fields['login']
    person.password = fields['password']
    person.firstname = fields['firstname']
    person.lastname = fields['lastname']
    db.session.commit()
    return person
