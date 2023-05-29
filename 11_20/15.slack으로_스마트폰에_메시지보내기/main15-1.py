"""
봇(로봇) 채널로 메시지 보내는 코드 만들기
"""

import requests
import json

# 자신의 python_bot의 생성된 webhook url을 넣는다.
slack_webhook_url = "https://hooks.slack.com/services/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"

# webhook 방식으로 메시지를 보내는 함수
def sendSlackWebhook(strText):
    headers = {
        "Content-type": "application/json"
    }

    data = {
        "text": strText
    }

    res = requests.post(slack_webhook_url, headers=headers,
                        data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"


print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지 입니다."))
