import json
import requests


def line_notify(url, args):

    token = args.token
    message = args.message

    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    data = {
        "message": message,
    }

    response = requests.post(url, params=json.dumps(data), headers=headers)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' %
            (response.status_code, response.text))
