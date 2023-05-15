"""
실시간 환율 정보 크롤링 코드 만들기
"""

import requests
from bs4 import BeautifulSoup

# 환율비를 가져오는 함수
def get_exchange_rate(target1, target2):
    # 헤더를 추가
    headers = {
        'Host': 'kr.investing.com',
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'text/html; charset=utf-8'
    }

    response = requests.get(
        "https://kr.investing.com/currencies/{}-{}".format(target1, target2),
        headers=headers
    )

    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
    # 에러 해결이 안됨
    # print(containers.text)

get_exchange_rate('usd', 'krw')
