"""
내부, 외부 IP 주소 확인
"""

import socket # 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러온다.
import requests # 사이트에 접속하기 위해 모듈을 불러온다.
import re # IP주소를 찾기 위한 정규식을 사용하기 위해 모듈을 불러온다.

# 소켓을 연결한다.
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# www.google.co.kr에 접속한다. https의 기본 접속 포트는 443이다.
in_addr.connect(("www.google.co.kr", 443))

print("내부 IP: ", in_addr.getsockname()[0])
# -> 내부 IP:  172.30.1.1

# http://ipconfig.kr 사이트에 접속
req = requests.get("http://ipconfig.kr");

# 정규식 표현을 사용하여 IP주소를 가져와 out_addr 변수와 바인딩
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print("외부 IP: ", out_addr)
# -> 외부 IP:  175.198.204.145