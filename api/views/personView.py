from flask import Blueprint

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
