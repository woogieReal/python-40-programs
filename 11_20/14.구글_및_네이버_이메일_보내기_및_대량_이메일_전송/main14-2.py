"""
구글 메일을 보내는 코드 만들기
주의) 구글 앱 비밀번호 설정을 안해서 실행 불가
"""

import smtplib
from email.mime.text import MIMEText
import getpass

send_email = "woogiereal@gmail.com"
send_pwd = getpass.getpass('Password:')

recv_email = "123wodnr@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

text = """
내가 나에게 보낸다.
구글 > 네이버
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
