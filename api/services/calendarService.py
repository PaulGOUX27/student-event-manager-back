from api.services import eventService
from icalendar import Calendar as ICalendar, Event as IEvent
from pytz import timezone
import pytz
from datetime import datetime, timedelta
from api.core import logger

fmt = '%Y%m%dT%H%M%SZ'
HEL = timezone('Europe/Helsinki')
utc = pytz.utc


def generateCalendar():
    events = eventService.getAll()
    now = HEL.localize((datetime.now() + timedelta(hours=2)))
    cal = ICalendar()
    cal['version'] = "2.0"
    cal['prodid'] = "//Aalto//CS-E4400//Student Event Manager"
    for event in events:
        iEvent = IEvent()
        iEvent['uid'] = event.id
        iEvent['Summary'] = event.title
        iEvent['location'] = event.place
        iEvent['Description'] = event.description
        iEvent['dtstart'] = event.start_date.strftime(fmt)
        iEvent['dtend'] = event.end_date.strftime(fmt)
        iEvent['dtstamp'] = now.strftime(fmt)
        cal.add_component(iEvent)

    return cal.to_ical()
