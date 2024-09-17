import sys
import requests
import json

def write_message(*persons):
    """
    Amazon Lex でメッセージを作成したい。
    """
    message = f"おはようございます。今日のシャッフルチャットは<br />{' '.join([person + 'さん' for person in persons])}<br />です。よろしくお願いします。"
    return message

def send_notification(*persons):
    url = 'https://api.ovice.io/api/public/v1/organizations/notification'
    headers = {
        'accept': '*/*',
        'client_id': sys.argv[1],
        'client_secret': sys.argv[2],
        'Content-Type': 'application/json',
    }
    data = {
        'message': write_message(*persons),
        'service_name': 'シャッフルチャット',
        'service_logo_url': 'https://twinengine.jp/wp-content/themes/twin_engine/assets/images/common/bnr/peakys.jpg'
    }
    print(persons)
    # response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
