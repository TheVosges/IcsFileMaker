from icalendar import Calendar, Event
import pytz
from datetime import datetime
import os
from pathlib import Path

BEGIN = 'VCALENDAR'
VERSION = '2.0'
CALSCALE = 'GREGORIAN'
METHOD = 'PUBLISH'
X_WR_CALNAME = 'IcsFileMaker'
X_WR_TIMEZONE = 'Europe/Warsaw'
TZID = 'Europe/Warsaw'

def openCal():
    cal = Calendar()
    cal.add('version', VERSION)
    cal.add('calscale', CALSCALE)
    cal.add('method', METHOD)
    cal.add('x-wr-calname', X_WR_CALNAME)
    cal.add('x-wr-timezone', X_WR_TIMEZONE)
    cal.add('tzid', TZID)
    return cal

def addCal(cal, event):
    cal.add_component(event)

def closeCal(cal, filename = 'drugCalendar' ):
    directory = str(Path(__file__).parent) + "/"
    f = open(os.path.join(directory, 'Data/' + filename + '.ics'), 'wb')
    f.write(cal.to_ical())
    print(f.name)
    f.close()

def addEvent(summary, description, year, month, day, hour, minute):
    summary = "Przypomnienie o leku: " + summary
    if isinstance(year, int):
        if isinstance(month, int):
            if isinstance(day, int):
                if isinstance(hour, int):
                    if isinstance(minute, int):
                        print("")
        
    event = Event()
    print(summary, description, year, month, day, hour, minute)
    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', datetime(year, month, day, hour-1, minute, 0, tzinfo=pytz.utc ))
    event.add('dtend', datetime(year, month, day, hour-1, minute+15, 0, tzinfo=pytz.utc ))
    event.add('dtstamp', datetime(year, month, day, hour-1, minute, 0, tzinfo=pytz.utc ))
    event.add('transp', 'OPAQUE')
    # Adding events to calendar
    return event