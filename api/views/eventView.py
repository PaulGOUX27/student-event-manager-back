from flask import Blueprint, request

from api.core import serialize_list, create_response, logger
from api.services import eventService

event_blueprint = Blueprint("event_blueprint", __name__, url_prefix="/events")


@event_blueprint.route("", methods=["GET"])
def get_all_events():
    return create_response(data={"events": serialize_list(eventService.getAll())})


@event_blueprint.route("/<int:id_event>", methods=["DELETE"])
def delete_event_by_id(id_event):
    eventService.deleteId(id_event)
    return create_response(status=204)


@event_blueprint.route("", methods=["POST"])
def create_event():
    new_event = eventService.create(request.json)
    return create_response(status=201, data=new_event.to_dict())


@event_blueprint.route("/<int:id_event>", methods=["GET"])
def get_one_by_id(id_event):
    event = eventService.getOne(id_event)
    if event is None:
        return create_response(status=404, message="Event {} not found".format(id_event))
    return create_response(data=event.to_dict())
