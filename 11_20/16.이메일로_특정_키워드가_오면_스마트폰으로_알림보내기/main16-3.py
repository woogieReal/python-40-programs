"""
특정 키워드의 이메일을 받으면 메시지 보내는 코드 만들기
"""

import imaplib
import email
from email import policy
import requests
import json
import getpass


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


# 문자열을 인코딩
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject, encode


# 네이버의 메일로 로그인
# 구글 이메일을 읽을 시 'imap.gmail.com'
imap = imaplib.IMAP4_SSL('imap.naver.com')
id = '123wodnr@naver.com'
pw = getpass.getpass('Password:')
imap.login(id, pw)

# 받은 메일함에서 메일을 읽는다.
imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()

# 최신 5개의 이메일만 읽는다.
last_email = all_email[-5:]

# reversed()로 리스트를 뒤집어 최신의 메일부터 출력
for mail in reversed(last_email):
    # 메일을 읽음
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    # 보낸사람, 받은시간, 제목을 문자열 형태로 바인딩
    email_from = str(email_message['From'])
    email_date = str(email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    subject_str = str(subject)

    # 제목에서 "교보"을 찾았다면 slack으로 메시지로 전송
    # "교보"을 못 찾으면 -1을 반환
    if subject_str.find("교보") >= 0:
        slack_send_message = email_from + '\n' + email_date + '\n' + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)

# 로그아웃
imap.close()
imap.logout()
