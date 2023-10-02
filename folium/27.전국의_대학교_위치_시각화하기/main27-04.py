"""
특정 학교의 위치에 마커를 표시하는 코드 만들기
"""

import folium
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 처음 보여주는 위도와 경도를 설정, zoom_start는 지도의 배율
map = folium.Map(location=[37, 127], zoom_start=7)

# 위도와 경도에 popup이름으로 파란색의 아이콘으로 마커를 표시
marker = folium.Marker([37.341435483, 126.733026596],
                       popup='한국공학대학교',
                       icon=folium.Icon(color='blue'))

# 마커를 추가
marker.add_to(map)

map.save('uni_map.html')
