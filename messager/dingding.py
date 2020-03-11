import json
import requests


def dingding_notify(url, args):

    message = args.message
    username = args.username

    headers = {
        "Content-Type": "application/json",
        "charset":"utf-8"
    }

    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": username,
            "text": message
        }
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' %
            (response.status_code, response.text))
