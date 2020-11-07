from flask import Blueprint, request

from api.core import serialize_list, create_response
from api.services import personService

persons = Blueprint("persons", __name__)


@persons.route("/persons", methods=["GET"])
def get_persons():
    return create_response(data={"persons": serialize_list(personService.getAll())})


@persons.route("/persons/<int:id_person>", methods=["DELETE"])
def delete_person_by_id(id_person):
    personService.deleteId(id_person)
    return create_response(status=204)


@persons.route("/persons", methods=["POST"])
def create_person():
    new_person = personService.create(request.json)
    return create_response(status=201, data=new_person.to_dict())


@persons.route("/persons/<int:id_person>", methods=["GET"])
def get_one_by_id(id_person):
    person = personService.getOne(id_person)
    if persons is None:
        return create_response(status=404, message="Person {} not found".format(id_person))
    return create_response(data=person.to_dict())
