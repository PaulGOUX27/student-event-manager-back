from api.services import eventService
from icalendar import Calendar as ICalendar, Event as IEvent
from pytz import timezone
from datetime import datetime


def generateCalendar():
    events = eventService.getAll()
    HEL = timezone('Europe/Helsinki')
    now = HEL.localize(datetime.now())
    cal = ICalendar()
    cal['version'] = "2.0"
    cal['prodid'] = "//Aalto//CS-E4400//Student Event Manager"
    for event in events:
        iEvent = IEvent()
        iEvent['uid'] = event.id
        iEvent['Summary'] = event.title
        iEvent['location'] = event.place
        iEvent['Description'] = event.description
        iEvent['dtstart'] = event.start_date.isoformat().replace('-', '').replace(':', '') + 'Z'
        iEvent['dtend'] = event.end_date.isoformat().replace('-', '').replace(':', '') + 'Z'
        iEvent['dtstamp'] = now.isoformat().replace('-', '').replace(':', '') + 'Z'
        cal.add_component(iEvent)

    return cal.to_ical()
