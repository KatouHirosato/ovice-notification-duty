import os
import sys
import datetime
import jpholiday

from . import selectduty
from . import notification
from . import download

CSVFILE = 'schedule.csv'

def main():
    day = datetime.datetime.now().weekday()
    if day != 0:
        download.download_sheet_as_csv(CSVFILE)
        selectduty.normalize_per_person(CSVFILE)
    if jpholiday.is_holiday(datetime.datetime.now().date()):
        return
    persons = selectduty.select(day, CSVFILE)
    notification.send_notification(*persons)


if __name__ == '__main__':
    main()
