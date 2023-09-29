"""
이메일 본문 내용을 읽는 코드 만들기
"""

import imaplib
import email
from email import policy
import getpass


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
# Inbox(기본값), Sent, Drafts, Trash, Junk
imap.select('INBOX')
resp, data = imap.uid('search', None, 'All')
all_email = data[0].split()

# 최신 5개의 이메일만 읽는다.
last_email = all_email[-5:]

# 최신의 메일부터 출력하여 반복
# reversed()로 리스트를 뒤집어 최신의 메일부터 출력
for mail in reversed(last_email):
    # 메일을 읽음
    result, data = imap.uid('fetch', mail, '(RFC822)')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email, policy=policy.default)

    # 메일의 정보를 출력
    print('='*70)
    print('FROM:', email_message['From'])
    print('SENDER:', email_message['Sender'])
    print('TO:', email_message['To'])
    print('DATE:', email_message['Date'])
    subject, encode = find_encoding_info(email_message['Subject'])
    print('SUBJECT:', subject)

    print('[CONTENT]')

    # 메일의 본문의 내용을 읽어 출력
    # 메시지 타입이 'text/plain'일 경우에만 본문의 내용을 저장
    # 메일의 내용이 사진, html 등의 파일은 읽지 않는다.
    message = ''
    if email_message.is_multipart():
        for part in email_message.get_payload():
            if part.get_content_type() == 'text/plain':
                bytes = part.get_payload(decode=True)
                encode = part.get_content_charset()
                message = message + str(bytes, encode)
    print(message)
    print('='*70)

# 로그아웃
imap.close()
imap.logout()
