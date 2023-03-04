"""
The slack.py module provides functions for sending messages to a Slack channel using a webhook URL. The message() function is used to add a message to the text that will be sent to the Slack channel. The notify() function is used to send the message to the channel. The Slack webhook URL is loaded from the SLACK_URL environment variable.

Functions:

message(msg="") -> str: Adds a message to the text that will be sent to the Slack channel. If msg is not provided, returns the current text.
notify(username, channel="#netdevops-alerts") -> None: Sends the message to the specified channel with the given username. If SLACK_URL is not set, the function does nothing. If the request to Slack fails, a ValueError is raised.
Note: This module requires the requests library and a Slack webhook URL.
"""

import json
import os
import requests

text = ""

# Slack notification URL
SLACK_URL = os.environ.get("SLACK_URL")

def message(msg="") -> str:
    global text

    # just call the function to see what's stored
    if not msg:
        return text

    text = "{}{}\n".format(text, msg)

    return text


def notify(username, channel="#netdevops-alerts") -> None:
    global text

    if not SLACK_URL:
        return

    payload = {
        "channel": channel,
        "icon_emoji": ":ghost:",
        "text": "```{}```".format(text),
        "username": username,
    }

    response = requests.post(SLACK_URL, json=payload, headers={'Content-Type': 'application/json'})

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

    text = ''