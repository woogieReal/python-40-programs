import pandas as pd
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'output02-01.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

print(df.loc[0].tolist())
# -> ['row 1', 'a', 'b']

print(df.loc[1].tolist())
# -> ['row 2', 'c', 'd']