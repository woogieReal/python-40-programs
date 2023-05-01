"""
내부 IP를 확인
아래 방법으로 진행하여 내부 IP 확인 시
가상환경 등을 사용하여 여러 개의 환경이 있을 경우 다른 IP가 출력될 수 있다.
"""

import socket # 컴퓨터가 연결된 접속정보를 받아올 때 사용하는 모듈을 불러온다

# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩
in_addr = socket.gethostbyname(socket.gethostname());

# 내부 IP를 확인한다.
print(in_addr)

print(socket.gethostname())
# -> A66411-002.local

print(socket.gethostbyname(socket.gethostname()))
# -> 127.0.0.1