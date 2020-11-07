from flask import Blueprint, request

from api.core import serialize_list, create_response
from api.services import eventCategoryService

eventCategory_blueprint = Blueprint("eventCategory_blueprint", __name__, url_prefix="/event-categories")


@eventCategory_blueprint.route("", methods=["GET"])
def get_all_event_category():
    return create_response(data={"event-categories": serialize_list(eventCategoryService.getAll())})


@eventCategory_blueprint.route("/<int:id_ec>", methods=["DELETE"])
def delete_event_category_by_id(id_ec):
    eventCategoryService.deleteId(id_ec)
    return create_response(status=204)


@eventCategory_blueprint.route("", methods=["POST"])
def create_event_category():
    new_event_category = eventCategoryService.create(request.json)
    return create_response(status=201, data=new_event_category.to_dict())


@eventCategory_blueprint.route("/<int:id_ec>", methods=["GET"])
def get_one_by_id(id_ec):
    event_category = eventCategoryService.getOne(id_ec)
    if event_category is None:
        return create_response(status=404, message="EventCategory {} not found".format(id_ec))
    return create_response(data=event_category.to_dict())
