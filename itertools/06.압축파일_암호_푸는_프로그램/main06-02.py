"""
압축 푸는 코드 만들고 실행
해당 코드는 중첩 for문으로 비밀번호를 찾아 압축을 풀고도 계속 실행하기 때문에 정상동작하지 않음
다음 파일 참고
"""

import itertools
import zipfile
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 숫자, 영문, 소문자, 영문 대문자의 문자열을 바인딩
passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 비밀번호가 입력된 암축파일의 경로를 입력하여 불러온다.
zFile = zipfile.ZipFile('암호1234.zip')

for len in range(1, 6):
    to_attempt = itertools.product(passwd_string, repeat=len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        
        # 비밀번호를 입력하여 맞으면 try를 실행, 틀리면 except를 실행
        try:
            zFile.extractall(pwd=passwd.encode())
            print(f"비밀번호는 {passwd} 입니다.")
            break
        except:
            pass
