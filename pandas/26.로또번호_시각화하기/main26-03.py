"""
당첨번호의 빈도수를 출력하는 코드 만들기
"""

import pandas as pd
from collections import Counter
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'lotto.xlsx'

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

# 6개의 번호를 숫자형 타입으로 읽어 num_list에 더해준다.
num_list = list(df_from_excel['당첨번호1'].astype(int))
num_list += list(df_from_excel['당첨번호2'].astype(int))
num_list += list(df_from_excel['당첨번호3'].astype(int))
num_list += list(df_from_excel['당첨번호4'].astype(int))
num_list += list(df_from_excel['당첨번호5'].astype(int))
num_list += list(df_from_excel['당첨번호6'].astype(int))

# 가장 많이 나온 숫자 45개를 찾는다.
count = Counter(num_list)
most_num = count.most_common(45)

print(most_num)
# [(34, 163), ..., (9, 114)]
# 34가 163번으로 가장 많이 나오고, 9가 114번으로 가장 적게 나옴