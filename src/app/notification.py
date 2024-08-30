import requests
import json


def send_notification(client_id, client_secret, message):
    url = 'https://api.ovice.io/api/public/v1/organizations/notification'
    headers = {
        'accept': '*/*',
        'client_id': client_id,
        'client_secret': client_secret,
        'Content-Type': 'application/json',
    }
    data = {
        'message': message,
        'service_name': 'シャッフルトーク',
        'service_logo_url': 'https://twinengine.jp/wp-content/themes/twin_engine/assets/images/common/bnr/peakys.jpg'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())