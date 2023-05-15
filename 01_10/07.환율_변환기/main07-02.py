"""
1달러를 원화로 변환한 결과 출력 코드 만들기
"""

from currency_converter import CurrencyConverter

# 에러: urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:997)>
# 참고: https://cosmosproject.tistory.com/651
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 최신 환율 정보로 업데이트
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

# 1달러를 대한민국 원화로 변경할 때 금액을 출력
print(cc.convert(1,'USD','KRW'))