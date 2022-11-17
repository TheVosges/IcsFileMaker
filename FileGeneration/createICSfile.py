<<<<<<< HEAD
from pathlib import Path
import csv
from datetime import date
import datetime
from FileGeneration import icsFileMaker

BEGIN = 'VCALENDAR'
VERSION = '2.0'
CALSCALE = 'GREGORIAN'
METHOD = 'PUBLISH'
X_WR_CALNAME = 'IcsFileMaker'
X_WR_TIMEZONE = 'Europe/Warsaw'
TZID = 'Europe/Warsaw'

data_filename = 'output.csv'


def convertDate(test_date):
    num = 1
    year = ''
    month = ''
    day = ''
    for i in test_date:
        if num < 3:
            day = day + i
        elif num in range(4, 6):
            month = month + i
        elif num in range(7, 11):
            year = year + i
        num += 1
    year = int(year)
    month = int(month)
    day = int(day)
    return year, month, day

def openFile(data_filename):
    directory = str(Path(__file__).parent) + "/"
    print(directory + data_filename)
    with open(directory + data_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        header = next(data)
        output = []
        for row in data:
            output.append(row)
    return output

def getTime(time):
    num = 1
    hour = ''
    minute = ''
    for i in time:
        if num < 3:
            hour = hour + i
        elif num in range(4, 6):
            minute = minute + i
        num += 1
    hour = int(hour)
    minute = int(minute)
    return hour, minute

def createIcsFile(filename = 'drugCalendar' ,data_filename = "output.csv"):
    data = openFile(data_filename)
    cal = icsFileMaker.openCal()
    for row in data:
        summary = row[0]
        description = row[1]
        okres_od = row[2]
        okres_do = row[3]
        godzina = row[4]

        year_od, month_od, day_od = convertDate(okres_od)
        year_do, month_do, day_do = convertDate(okres_do)

        d0 = date(year_od, month_od, day_od)
        d1 = date(year_do, month_do, day_do)

        i = 0
        while d0 != (d1 + datetime.timedelta(days=1)):
            hour, minute = getTime(godzina)
            event = icsFileMaker.addEvent(summary, description, int(d0.strftime("%Y")), int(d0.strftime("%m")),
                                          int(d0.strftime("%d")), hour, minute)
            icsFileMaker.addCal(cal, event)
            d0 = d0 + datetime.timedelta(days=1)
    icsFileMaker.closeCal(cal, filename = filename)


if __name__ == "__main__":
=======
from pathlib import Path
import csv
from datetime import date
import datetime
from FileGeneration import icsFileMaker

BEGIN = 'VCALENDAR'
VERSION = '2.0'
CALSCALE = 'GREGORIAN'
METHOD = 'PUBLISH'
X_WR_CALNAME = 'IcsFileMaker'
X_WR_TIMEZONE = 'Europe/Warsaw'
TZID = 'Europe/Warsaw'

data_filename = 'output.csv'


def convertDate(test_date):
    num = 1
    year = ''
    month = ''
    day = ''
    for i in test_date:
        if num < 3:
            day = day + i
        elif num in range(4, 6):
            month = month + i
        elif num in range(7, 11):
            year = year + i
        num += 1
    year = int(year)
    month = int(month)
    day = int(day)
    return year, month, day

def openFile(data_filename):
    directory = str(Path(__file__).parent) + "/"
    print(directory + data_filename)
    with open(directory + data_filename, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        header = next(data)
        output = []
        for row in data:
            output.append(row)
    return output

def getTime(time):
    num = 1
    hour = ''
    minute = ''
    for i in time:
        if num < 3:
            hour = hour + i
        elif num in range(4, 6):
            minute = minute + i
        num += 1
    hour = int(hour)
    minute = int(minute)
    return hour, minute

def createIcsFile(filename = 'drugCalendar' ,data_filename = "output.csv"):
    data = openFile(data_filename)
    cal = icsFileMaker.openCal()
    for row in data:
        summary = row[0]
        description = row[1]
        okres_od = row[2]
        okres_do = row[3]
        godzina = row[4]

        year_od, month_od, day_od = convertDate(okres_od)
        year_do, month_do, day_do = convertDate(okres_do)

        d0 = date(year_od, month_od, day_od)
        d1 = date(year_do, month_do, day_do)

        i = 0
        while d0 != (d1 + datetime.timedelta(days=1)):
            hour, minute = getTime(godzina)
            event = icsFileMaker.addEvent(summary, description, int(d0.strftime("%Y")), int(d0.strftime("%m")),
                                          int(d0.strftime("%d")), hour, minute)
            icsFileMaker.addCal(cal, event)
            d0 = d0 + datetime.timedelta(days=1)
    icsFileMaker.closeCal(cal, filename = filename)


if __name__ == "__main__":
>>>>>>> devWera
    createIcsFile(data_filename)