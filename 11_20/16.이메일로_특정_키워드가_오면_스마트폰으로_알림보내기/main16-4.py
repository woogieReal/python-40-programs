"""
번복 실행하여 새로운 이메일이 있을 경우에만 메시지 보내는 코드 만들기
"""

import imaplib
import email
from email import policy
import requests
import json
import time
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

# 보내는 데이터를 저장할 리스트를 생성
send_list = []

while True:
    try:
        # 받은 메일함에서 메일을 읽는다.
        # Inbox(기본값), Sent, Drafts, Trash, Junk
        imap.select('INBOX')
        resp, data = imap.uid('search', None, 'All')
        all_email = data[0].split()

        # 최신 5개의 이메일만 읽는다.
        last_email = all_email[-5:]

        for mail in reversed(last_email):
            # 메일을 읽음
            result, data = imap.uid('fetch', mail, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_bytes(
                raw_email, policy=policy.default)

            # 보낸사람, 받은시간, 제목을 문자열 형태로 바인딩
            email_from = str(email_message['From'])
            email_date = str(email_message['Date'])
            subject, encode = find_encoding_info(email_message['Subject'])
            subject_str = str(subject)

            # 메일에서 "교보"를 찾았다면 조건에 만족
            if subject_str.find("교보") >= 0:
                slack_send_message = email_from + '\n' + email_date + '\n' + subject_str

                # 새로운 메시지가 있는 경우
                if slack_send_message not in send_list:
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)

                    # 보낸 메시지를 추가
                    # append는 리스트 마지막에 요소를 추가
                    send_list.append(slack_send_message)

        time.sleep(30)

    # 키보드 인터럽트가 발생하면 while문을 종료
    except KeyboardInterrupt:
        break

imap.close()
imap.logout()
