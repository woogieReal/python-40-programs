"""
오픈 API를 이용해 주소를 좌표로 변환하는 코드 만들기

folium 라이브러리를 이용하여 지도에 표시하기 위해서는 주소가 아닌 좌표의 데이터가 필요
주소를 좌표로 변환하기 위해 나라에서 운영하는 오픈 API 사용
"""

import requests
from dotenv import load_dotenv
import os

load_dotenv()

# API 접속내용
url = 'http://api.vworld.kr/req/address?'
params = 'service=address&request=getcoord&version=2.0&crs=epsg:4326&refine=true&simple=false&format=json&type='
road_type = 'ROAD'  # 도로명주소
road_type2 = 'PARCEL'  # 지번주소
address = '&address='
keys = '&key='

# 발급받은 인증키
primary_key = os.environ.get('GEO_DEV_KEY')


# 주소를 x, y 좌표로 반환해주는 함수
def request_geo(road):
    page = requests.get(url+params+road_type+address+road+keys+primary_key)
    json_data = page.json()
    if json_data['response']['status'] == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        x = 0
        y = 0
        return x, y


x, y = request_geo("경기도 시흥시 산기대학로 237 (정왕동, 한국산업기술대학교)")

print(f'x값: {x}')
print(f'y값: {y}')
