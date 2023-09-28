"""
외부 IP를 확인
특정사이트에 접속하여 내가 연결된 IP를 확인
"""

import requests # 사이트에 접속하기 위해 모듈을 불러온다.
import re # IP주소를 찾기 위한 정규식을 사용하기 위해 모듈을 불러온다.

# http://ipconfig.kr 사이트에 접속
req = requests.get("http://ipconfig.kr")

# 정규식 표현을 사용하여 IP주소를 가져와 out_addr 변수와 바인딩
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 외부 IP주소를 출력
print(out_addr)
# -> 175.198.204.145
