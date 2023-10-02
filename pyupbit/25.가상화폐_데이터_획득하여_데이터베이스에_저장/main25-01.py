"""
가상화폐 시세 조회 코드 만들기
"""

import pyupbit

# 거래 되고 있는 가상화폐 출력
const_lists = pyupbit.get_tickers(fiat='KRW')
print(const_lists)

# 비트코인과 이더리움의 한국 시세를 출력
price_now = pyupbit.get_current_price(['KRW-BTC', 'KRW-ETH'])
print(price_now)