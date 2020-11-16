from api.services import eventService
from icalendar import Calendar as ICalendar, Event as IEvent
import time


def generateCalendar():
    events = eventService.getAll()
    timestamp = time.localtime(time.time())
    cal = ICalendar()
    cal['version'] = "2.0"
    cal['prodid'] = "//Aalto//CS-E4400//Student Event Manager"
    for event in events:
        iEvent = IEvent()
        iEvent['uid'] = event.id
        iEvent['Summary'] = event.title
        iEvent['location'] = event.place
        iEvent['Description'] = event.description
        iEvent['dtstart'] = event.start_date.isoformat().replace('-', '').replace(':', '')
        iEvent['dtend'] = event.end_date.isoformat().replace('-', '').replace(':', '')
        iEvent['dtstamp'] = str(timestamp.tm_year) + str(timestamp.tm_mon) + str(timestamp.tm_mday) + 'T' \
                            + str(timestamp.tm_hour) + str(timestamp.tm_min) + str(timestamp.tm_sec)
        cal.add_component(iEvent)

    return cal.to_ical()
