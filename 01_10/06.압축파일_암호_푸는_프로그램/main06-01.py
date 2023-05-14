"""
압축 푸는 코드 만들고 실행
"""

import itertools

# 숫자, 영문, 소문자, 영문 대문자의 문자열을 바인딩
passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1~3까지 반복
for len in range(1, 4):
    # passwd_string 모든 문자열을 repeat=길이 로 정렬하여 반환
    to_attempt = itertools.product(passwd_string, repeat=len)
    
    # 정렬하여 반환된 문자의 수만큼 반복
    for attempt in to_attempt:
        # 리스트로 반환된 값을 문자열로 변환 ''.join(리스트)는 리스트의 값을 문자열로 변환
        passwd = ''.join(attempt)
        print(passwd)
