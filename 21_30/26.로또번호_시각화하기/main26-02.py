"""
판다스로 값 읽고 그래프로 그리는 코드 만들기
"""

import pandas as pd
import matplotlib.pyplot as plt # 그래프를 그리기 위한 라이브러리
from matplotlib import font_manager, rc

file_path = '21_30/26.로또번호_시각화하기/lotto.xlsx'

# 엔진은 openpyxl을 사용하여 판다스의 데이터프레임으로 엑셀 파일을 불러온다.
df_from_excel = pd.read_excel(file_path, engine='openpyxl')

# 0,1번 줄을 삭제
df_from_excel = df_from_excel.drop(index=[0,1])

# columns의 이름을 다시 정의
df_from_excel.columns = [
                        '년도','회차','추첨일',
                        '1등당첨자수','1등당첨금액','2등당첨자수','2등당첨금액',
                        '3등당첨자수','3등당첨금액','4등당첨자수','4등당첨금액',
                        '5등당첨자수','5등당첨금액',
                        '당첨번호1','당첨번호2','당첨번호3','당첨번호4','당첨번호5','당첨번호6','보너스번호'
                        ]

# 금액에서 쉼표와 '원'을 제거
df_from_excel['1등당첨금액']=df_from_excel['1등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['2등당첨금액']=df_from_excel['2등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['3등당첨금액']=df_from_excel['3등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['4등당첨금액']=df_from_excel['4등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)
df_from_excel['5등당첨금액']=df_from_excel['5등당첨금액'].str.replace(pat=r'[ㄱ-ㅣ가-힣,]+', repl= r'', regex=True)

df_from_excel["1등당첨금액"] = pd.to_numeric(df_from_excel["1등당첨금액"])
df_from_excel["2등당첨금액"] = pd.to_numeric(df_from_excel["2등당첨금액"])
df_from_excel["3등당첨금액"] = pd.to_numeric(df_from_excel["3등당첨금액"])
df_from_excel["4등당첨금액"] = pd.to_numeric(df_from_excel["4등당첨금액"])
df_from_excel["5등당첨금액"] = pd.to_numeric(df_from_excel["5등당첨금액"])

print( df_from_excel[['1등당첨금액','2등당첨금액','3등당첨금액','4등당첨금액','5등당첨금액']] )

# 그래프의 이름을 표시할 때 한글을 사용하기 위한 폰트를 설정
# https://pinkwink.kr/990
rc('font', family='AppleGothic')

# 회차의 마지막 100개의 데이터만 x축으로 사용
x = df_from_excel['회차'].iloc[:100].values

# 당첨금액의 마지막 100개의 데이터만 y축으로 사용
price = df_from_excel['1등당첨금액'].iloc[:100].values / 100000000

# 그래프의 초기 표시 크기를 결정
plt.figure(figsize=(10, 6))

# x축, y축 라벨을 설정
plt.xlabel('회차')
plt.ylabel('당첨금액(단위:억원)')

# 바의 x, y값과 바의 폭을 지정하여 그래프를 그린다.
plt.bar(x, price, width=0.4)

# 그래프를 표시
plt.show()