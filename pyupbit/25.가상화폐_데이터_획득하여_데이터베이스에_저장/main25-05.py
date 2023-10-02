"""
데이터베이스의 중복을 제거
"""

import pandas as pd
import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

db_path = 'coin.db'
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col='index')

readed_df.to_sql('BTC_NEW', con, if_exists='replace')

print(readed_df)