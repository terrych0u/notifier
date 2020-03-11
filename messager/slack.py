import datetime
import json
import requests


def slack_notify(url, args):

    message = args.message
    channel = args.channel
    username = args.username
    color = args.color

    ts = datetime.datetime.now().timestamp()
    # print(ts)

    headers = {
        "Content-Type": "application/json",
        "charset":"utf-8"
    }

    data = {
        "channel": channel,
        "username": username,
        "attachments": [
          {
            "text": message,
            "color": color,
            "ts": ts
            # "fallback": "Plain-text summary of the attachment.",
            # "pretext": "Optional text that appears above the attachment block",
            # "author_name": "Bobby Tables",
            # "author_link": "http://flickr.com/bobby/",
            # "author_icon": "http://flickr.com/icons/bobby.jpg",
            # "title": "Slack API Documentation",
            # "title_link": "https://api.slack.com/",
            # "fields": [
            #     {
            #         "title": "Priority",
            #         "value": "High",
            #         "short": "false"
            #     }
            # ],
            # "image_url": "http://my-website.com/path/to/image.jpg",
            # "thumb_url": "http://example.com/path/to/thumb.png",
            # "footer": "Slack API",
            # "footer_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
          }
        ],
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s' %
            (response.status_code, response.text))
