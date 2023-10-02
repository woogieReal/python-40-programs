"""
비트코인의 분봉 데이터를 데이터베이스에 저장하는 코드 만들기
"""

import pyupbit
import sqlite3
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2021-12-02 11:20'
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

db_path = 'coin.db'

con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists='append')

con.close