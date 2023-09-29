"""
네이버 메일을 보내는 코드 만들기
"""

import smtplib
from email.mime.text import MIMEText
import getpass

send_email = "123wodnr@naver.com"
send_pwd = getpass.getpass('Password:')

recv_email = "woogiereal@gmail.com"

# 네이버 메일의 smtp 주소와 포트번호
smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
내가 나에게 보낸다.
네이버 > 구글
"""
msg = MIMEText(text)

msg['Subject'] = f"{send_email} > {recv_email}"
msg['From'] = send_email
msg['To'] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
