import pandas as pd
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 기본
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])
df1.to_excel("output1.xlsx")

# 시트 이름 지정
df1.to_excel("output2.xlsx",
             sheet_name='Sheet_name_1')

# 하나 이상의 시트를 작성하기 위해서는 ExcelWriter 객체를 사용해야 한다.
df2 = df1.copy()
with pd.ExcelWriter('output3.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet_name_1')
    df2.to_excel(writer, sheet_name='Sheet_name_2')

# 기존 엑셀 파일에 더할 때도 ExcelWriter 를 사용한다.
with pd.ExcelWriter('output3.xlsx',
                    mode='a') as writer:
    df2.to_excel(writer, sheet_name='Sheet_name_3')
