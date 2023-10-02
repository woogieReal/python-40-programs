"""
데이터베이스의 데이터 읽고 출력하는 코드 만들기
"""

import pandas as pd
import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

db_path = 'coin.db'
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col='index')

print(readed_df)