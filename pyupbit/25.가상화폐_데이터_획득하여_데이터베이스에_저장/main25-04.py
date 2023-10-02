"""
비트코인 데이터를 읽어 데이터베이스에 저장하는 코드 만들기
"""

import pyupbit
import sqlite3
import datetime
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# datetime 라이브러리를 사용하여 시작날짜와 종료날짜의 모든 날을 리스트형태로 반환한다.
def date_range(start, end):
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    start = start + datetime.timedelta(days=1)
    
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    end = end + datetime.timedelta(days=1)

    dates = [(start + datetime.timedelta(days=i)).strftime('Y-%m-%d') for i in range((end-start).days+1)]
    return dates

dates = date_range('2021-11-30', '2021-12-01')

print(dates)

for day in reversed(dates):
    myDay = day + ' 00:00'
    print(myDay)
    
    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = '2021-12-02 11:20'
    count = 200
    price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)
    
    print(price_now)
    db_path = 'coin.db'
    
    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', con, if_exists='append')
    
    con.close