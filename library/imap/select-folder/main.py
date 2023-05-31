"""
네이버 이메일을 읽는 코드 만들기
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

# https://stackoverflow.com/questions/44230855/python-imaplib-selecting-folders
for i in imap.list()[1]:
    print(i)
# -> Inbox
# -> Sent
# -> Drafts
# -> Trash
# -> Junk