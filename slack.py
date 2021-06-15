#coding: UTF-8

import slackweb
import requests
from os import getenv

# --- Slack Setting ---
SLACK_WEBHOOK='https://hooks.slack.com/services/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'
#SLACK_WEBHOOK=getenv('SLACK_WEBHOOK')
SLACK_CHANNEL='#hoiku-watch'
SLACK_USER='一時保育空き警報発令！！'
SLACK_TEXT="空きがでたっぽいよ！！急げ"

class Slack:
    def post():
        #print('post..')
        slack=slackweb.Slack(url=SLACK_WEBHOOK)
        #slack.notify(text="This is a test.")
        attachments=[]
        attachment={"pretext": "急げ！！",
                    "color": "#36a64f",
                    "fields":[
                          {
                          "title": "急",
                          "value": "げ!!",
                          }
                      ]
                    }
        attachments.append(attachment)
        slack.notify(text=SLACK_TEXT, channel=SLACK_CHANNEL, username=SLACK_USER, attachments=attachments)