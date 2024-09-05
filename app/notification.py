import sys
import requests
import json
import openai
openai.api_key = sys.argv[3]

def add_greeting_to_message(input_message):
    # response = openai.chat.completions.create(
    #     model="gpt-3.5-turbo",  # または "gpt-4"
    #     messages=[
    #         {"role": "system", "content": "短い挨拶を追加してください。"},
    #         {"role": "user", "content": input_message}
    #     ]
    # )
    # output_message = response['choices'][0]['message']['content'].strip()
    # return output_message
    return input_message+"よろしくお願いします。"

def send_notification(*persons):
    url = 'https://api.ovice.io/api/public/v1/organizations/notification'
    headers = {
        'accept': '*/*',
        'client_id': sys.argv[1],
        'client_secret': sys.argv[2],
        'Content-Type': 'application/json',
    }
    
    message = f"おはようございます。今日のシャッフルチャットは<br />{' '.join([person + 'さん' for person in persons])}<br />です。"
    data = {
        'message': add_greeting_to_message(message),
        'service_name': 'シャッフルチャット',
        'service_logo_url': 'https://twinengine.jp/wp-content/themes/twin_engine/assets/images/common/bnr/peakys.jpg'
    }

    print(data) # TEST
    return # TEST

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response.json())
