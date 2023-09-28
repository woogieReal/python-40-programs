"""
내부 IP를 확인
socket으로 외부 사이트에 접속하고 접속된 정보를 바탕으로 IP를 확인
앞선 방법보다 조금 더 정확하게 내부 IP를 확인하는 방법
"""

import socket # 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러온다

# 소켓을 연결한다.
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# www.google.co.kr에 접속한다. https의 기본 접속 포트는 443이다.
in_addr.connect(("www.google.co.kr", 443))

# 연결된 소켓의 이름을 출력한다.
print(in_addr.getsockname()[0])
# -> 172.30.1.1

