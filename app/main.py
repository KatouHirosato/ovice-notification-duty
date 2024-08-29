import sys
import datetime

from . import selectduty
from . import notification

def main():
    DAY = datetime.datetime.now().weekday()
    if DAY == 0:
        selectduty.reset()
        selectduty.normalize_per_people()
    weight = selectduty.todays_weights(DAY)
    persons = selectduty.select(weight)
    message = f"おはようございます。今日のシャッフルトークは\n{persons[0]}さん {persons[1]}さん {persons[2]}sさん\nです。良い一日を！"
    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    notification.send_notification(client_id, client_secret, message)


if __name__ == '__main__':
    main()