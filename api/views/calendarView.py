from flask import Blueprint, Response, request

from api.services import calendarService

calendar_blueprint = Blueprint("calendar_blueprint", __name__, url_prefix="/calendar")


@calendar_blueprint.route("", methods=["GET"])
def generate_events():
    event_category_ids = request.args.getlist('event_categories')
    return Response(calendarService.generateCalendar(event_category_ids), status=200, mimetype="text/calendar")
