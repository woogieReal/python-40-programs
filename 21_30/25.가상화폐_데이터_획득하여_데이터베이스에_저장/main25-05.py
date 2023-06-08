"""
데이터베이스의 중복을 제거
"""

import pandas as pd
import sqlite3

db_path = '21_30/25.가상화폐_데이터_획득하여_데이터베이스에_저장/coin.db'
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT DISTINCT * FROM 'BTC'", con, index_col='index')

readed_df.to_sql('BTC_NEW', con, if_exists='replace')

print(readed_df)