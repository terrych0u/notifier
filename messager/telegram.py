import json
import requests


def telegram_notify(url, args):

    message = args.message
    telegram_id = args.id

    data = {
        "chat_id": telegram_id,
        "text": message,
        "parse_mode": "HTML"
    }

    response = requests.post(url, data=json.dumps(data))

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' %
            (response.status_code, response.text))
