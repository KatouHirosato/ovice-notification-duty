import os
import sys
import datetime

from . import selectduty
from . import notification
from . import download

CSVFILE = 'schedule.csv'

def main():
    day = datetime.datetime.now().weekday()
    if day == 0 or not os.path.exists(CSVFILE):
        download.download_sheet_as_csv(CSVFILE)
        selectduty.normalize_per_person(CSVFILE)
    persons = selectduty.select(day, CSVFILE)
    message = f"おはようございます。今日のシャッフルチャットは<br />{persons[0]}さん {persons[1]}さん {persons[2]}さん<br />です。"
    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    notification.send_notification(client_id, client_secret, message)


if __name__ == '__main__':
    main()
