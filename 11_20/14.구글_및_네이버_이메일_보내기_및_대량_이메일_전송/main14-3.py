"""
파일을 첨부하여 메일 보내는 코드 만들기
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import getpass

send_email = "123wodnr@naver.com"
send_pwd = getpass.getpass('Password:')

recv_email = "woogiereal@gmail.com"

# 네이버 메일의 smtp 주소와 포트번호
smtp_name = "smtp.naver.com"
smtp_port = 587

# 메시지 형식을 복합형식으로 선언, 첨부파일을 보낼 수 있다.
msg = MIMEMultipart()

msg['Subject'] = f"첨부파일 테스트: {send_email} > {recv_email}"
msg['From'] = send_email
msg['To'] = recv_email

text = """
첨부파일 메일 테스트 내용 입니다.
감사합니다.
"""
contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = '11_20/14.구글_및_네이버_이메일_보내기_및_대량_이메일_전송/첨부파일.txt'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition',
                        'attachment', filename="첨부파일.txt")
    msg.attach(etc_part)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
