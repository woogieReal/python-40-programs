"""
자료의 모든 대학교 주소에 마커 표시하는 코드 만들기
"""

import pandas as pd
import folium

# 엑셀 파일을 읽어온다.
file_path = '21_30/27.전국의_대학교_위치_시각화하기/학교주소좌표.xlsx'
df_from_excel = pd.read_excel(file_path, engine='openpyxl', header=None)

# 컬럼 이름 지정
df_from_excel.columns = ['학교이름', '주소', 'x', 'y']

name_list = df_from_excel['학교이름'].to_list()
addr_list = df_from_excel['주소'].to_list()
position_x_list = df_from_excel['x'].to_list()
position_y_list = df_from_excel['y'].to_list()

# 처음 보여주는 위도와 경도를 설정, zoom_start는 지도의 배율
map = folium.Map(location=[37, 127], zoom_start=7)

for i in range(len(name_list)):
    if position_x_list[i] != 0:
        # 위도와 경도에 헉교이름으로 파란색의 아이콘으로 마커를 표시
        marker = folium.Marker([position_y_list[i], position_x_list[i]],
                               popup=name_list[i],
                               icon=folium.Icon(color='blue'))

        # 마커를 추가
        marker.add_to(map)


map.save('21_30/27.전국의_대학교_위치_시각화하기/uni_map.html')
