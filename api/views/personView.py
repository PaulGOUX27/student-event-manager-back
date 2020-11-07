from flask import Blueprint, request

from api.core import serialize_list, create_response
from api.services import personService

person_blueprint = Blueprint("person_blueprint", __name__, url_prefix="/persons")


@person_blueprint.route("", methods=["GET"])
def get_persons():
    return create_response(data={"persons": serialize_list(personService.getAll())})


@person_blueprint.route("/<int:id_person>", methods=["DELETE"])
def delete_person_by_id(id_person):
    personService.deleteId(id_person)
    return create_response(status=204)


@person_blueprint.route("", methods=["POST"])
def create_person():
    new_person = personService.create(request.json)
    return create_response(status=201, data=new_person.to_dict())


@person_blueprint.route("/<int:id_person>", methods=["GET"])
def get_one_by_id(id_person):
    person = personService.getOne(id_person)
    if person is None:
        return create_response(status=404, message="Person {} not found".format(id_person))
    return create_response(data=person.to_dict())
