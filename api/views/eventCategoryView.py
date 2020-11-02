from flask import Blueprint

from api.core import serialize_list, create_response
from api.services import eventCategoryService

eventCategories = Blueprint("eventCategories", __name__)


@eventCategories.route("/event-categories", methods=["GET"])
def get_all_event_category():
    return create_response(data={"event-categories": serialize_list(eventCategoryService.getAll())})


@eventCategories.route("/event-categories/<int:id_ec>", methods=["DELETE"])
def delete_event_category_by_id(id_ec):
    eventCategoryService.deleteId(id_ec)
    return create_response(status=204)
