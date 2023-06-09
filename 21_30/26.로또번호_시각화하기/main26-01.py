"""
판다스로 값 읽고 그래프로 그리는 코드 만들기
"""

import pandas as pd

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

# 앞 부분의 데이터만 출력
print(df_from_excel.head())

# 회사를 출력
print(df_from_excel['회차'].values)

# 1등 당첨금액을 출력
print(df_from_excel['1등당첨금액'].values)