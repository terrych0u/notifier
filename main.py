#!/usr/bin/env python3

import argparse
import sys
import os

from messager.slack import slack_notify
from messager.line import line_notify
from messager.telegram import telegram_notify
from messager.dingding import dingding_notify





if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog=sys.argv[0], description='Tutorial')
    parser.add_argument("message", help="The message body that you want to send.")
    parser.add_argument("--channel", help='The channel name on slack, only work when target is "slack".')
    parser.add_argument("--username", help='The username show on slack message, only work when target is "slack".')
    parser.add_argument("--color", help='The message with color show on slack, only work when target is "slack".', default='#008000')
    parser.add_argument("--target", help='Currently support "Slack", "Line", "DingDing".')
    parser.add_argument("--token", help='The token use for Line Notify auth, only work when target is "Line"')
    parser.add_argument("--id", help='The chat id, only work when target is "Telergam"')

    args = parser.parse_args()

    url = os.getenv('URL')
    target = args.target.lower()

    target_dict = {
        "slack": "slack_notify",
        "line": "line_notify",
        "telegram": "telegram_notify",
        "dingding": "dingding_notify"
    }

    if url is None or target is None or target not in target_dict.keys():
        parser.print_help()
    else:
        run = target_dict[target]
        eval(run + '(url, args)')
