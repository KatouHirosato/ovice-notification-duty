import sys
import requests
import json
import openai
openai.api_key = sys.argv[3]

def add_greeting_to_message(input_message):
    response = openai.chat_completion.create(
        model="gpt-3.5-turbo",  # または "gpt-4"
        messages=[
            {"role": "system", "content": "短い挨拶を追加してください。"},
            {"role": "user", "content": input_message}
        ]
    )
    output_message = response['choices'][0]['message']['content'].strip()
    return output_message

def send_notification(client_id, client_secret, message):
    url = 'https://api.ovice.io/api/public/v1/organizations/notification'
    headers = {
        'accept': '*/*',
        'client_id': client_id,
        'client_secret': client_secret,
        'Content-Type': 'application/json',
    }
    data = {
        'message': add_greeting_to_message(message),
        'service_name': 'シャッフルチャット',
        'service_logo_url': 'https://twinengine.jp/wp-content/themes/twin_engine/assets/images/common/bnr/peakys.jpg'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
