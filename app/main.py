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
    if jpholiday.is_holiday(datetime.datetime.now().date()):
        return
    download.download_sheet_as_csv(CSVFILE)
    selectduty.normalize_per_person(CSVFILE)
    persons = selectduty.select(day, CSVFILE)
    notification.send_notification(*persons)

if __name__ == '__main__':
    main()
