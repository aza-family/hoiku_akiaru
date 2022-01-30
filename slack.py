#coding: UTF-8

import slackweb
import requests
from os import getenv
# --- Slack Setting ---

SLACK_WEBHOOK=getenv('SLACK_WEBHOOK')
SLACK_CHANNEL='#hoiku-watch'
SLACK_USER='一時保育空き警報発令！！'
# SLACK_TEXT="空きがでたっぽいよ！！急げ"

class Slack:

    def __init__(self, type):
        url_type = {10: "東陽", 20: "大島"}
        self.type = type
        self.txt = "{}の予約空きが出ました!!".format(url_type[type])
        self.url = "https://koto-kosodate-portal.jp/smf/mizube/general/refresh_cal.php?center_cd={}".format(type)

        # self.url = ""
    def post(self):
        # print("{}の予約空きが出ました!!".format(self.type))
        # print(self.txt)
        # print(self.url)

        slack=slackweb.Slack(url=SLACK_WEBHOOK)
        #slack.notify(text="This is a test.")
        attachments=[]
        attachment={"pretext": self.txt,
                    "color": "#36a64f",
                    "fields":[
                          {
                          "title": "リンク:",
                          "value": self.url,
                          }
                      ]
                    }
        attachments.append(attachment)
        slack.notify(text=self.txt, channel=SLACK_CHANNEL, username=SLACK_USER, attachments=attachments)