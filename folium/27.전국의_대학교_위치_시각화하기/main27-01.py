"""
판다스에서 학교명과 주소 찾는 코드 만들기
"""

import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '고등교육기관_하반기_주소록-2022.xlsx'
df_from_excel = pd.read_excel(file_path, engine='openpyxl')

# 5번째 위치의 데이터를 columns으로 설정
df_from_excel.columns = df_from_excel.loc[4].tolist()
# -> ['연도', '학교종류', '시도', '행정구', '학교명', '학교명(영문)', '본분교', '학교상태', '설립', '우편번호', '주소', '전화번호', '팩스번호', '홈페이지']

# 0~5줄의 데이터를 버린다. 설명이나 이름등의 데이터 제거
df_from_excel = df_from_excel.drop(index=list(range(0, 5)))

print(df_from_excel.head())

print(df_from_excel['학교명'].values)

print(df_from_excel['주소'].values)
