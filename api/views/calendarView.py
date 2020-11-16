from flask import Blueprint, Response

from api.services import calendarService

calendar_blueprint = Blueprint("calendar_blueprint", __name__, url_prefix="/calendar")


@calendar_blueprint.route("", methods=["GET"])
def generate_events():
    return Response(calendarService.generateCalendar(), status=200, mimetype="text/calendar")
