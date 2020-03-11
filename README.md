# The general tool for sending message to IM.

Currently support `Slack`, `Line`, `Telegram`, `DingDing`,
also support `curl`, just change entrypoint on docker.


### Required

Environment variable `URL` have to setup!

##### Usage

Example send to slack：
```bash
env URL https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx ./main.py --targe slack --channel test <your message>
```


```bash
usage: ./main.py [-h] [--channel CHANNEL] [--username USERNAME]
                 [--color COLOR] [--target TARGET] [--token TOKEN]
                 message

Tutorial

positional arguments:
  message              The message body that you want to send.

optional arguments:
  -h, --help           show this help message and exit
  --channel CHANNEL    The channel name on slack, only work when target is
                       "slack".
  --username USERNAME  The username show on slack message, only work when
                       target is "slack".
  --color COLOR        The message with color show on slack, only work when
                       target is "slack".
  --target TARGET      Currently support "Slack", "Line", "DingDing".
  --token TOKEN        The token use for "Line Notify" auth, only work when
                       target is "Line"
```