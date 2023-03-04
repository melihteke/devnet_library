import json
import os
import requests
import environment

class SlackNotifier:

    # Slack notification URL
    SLACK_URL = os.environ.get("SLACK_URL")
    text = ""

    def __init__(self, slack_url=SLACK_URL):
        self.slack_url = slack_url
        self.text = ""

    def message(self, msg="") -> str:
        # just call the function to see what's stored
        if not msg:
            return self.text

        self.text = "{}{}\n".format(self.text, msg)

        return self.text

    def notify(self, username, channel="#sdwan_infra_test_tool_notifications") -> None:
        if not self.slack_url:
            return

        payload = {
            "channel": channel,
            "icon_emoji": ":robot_face:",
            "text": "```{}```".format(self.text),
            "username": username,
        }

        response = requests.post(self.slack_url, json=payload, headers={'Content-Type': 'application/json'})

        if response.status_code != 200:
            raise ValueError(
                'Request to slack returned an error %s, the response is:\n%s'
                % (response.status_code, response.text)
            )

        self.text = ''
