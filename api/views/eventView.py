from flask import Blueprint

from api.core import serialize_list, create_response, logger
from api.services import eventService

events = Blueprint("events", __name__)


@events.route("/events", methods=["GET"])
def get_all_events():
    return create_response(data={"events": serialize_list(eventService.getAll())})


@events.route("/events/<int:id_event>", methods=["DELETE"])
def delete_event_by_id(id_event):
    eventService.deleteId(id_event)
    return create_response(status=204)
