"""
비밀번호를 찾으면 프로그램이 종료되는 코드 만들고 실행
"""

import itertools
import zipfile


def un_zip(passwd_string, min_len, max_len, zFile):
    for len in range(min_len, max_len):
        to_attempt = itertools.product(passwd_string, repeat=len)
        for attempt in to_attempt:
            passwd = ''.join(attempt)
            print(passwd)
            try:
                zFile.extractall(pwd=passwd.encode())
                print(f" 비밀번호는 {passwd} 입니다. ")
                return 1
            except:
                pass


# 숫자, 영문, 소문자, 영문 대문자의 문자열을 바인딩
passwd_string = "012345789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 비밀번호가 입력된 암축파일의 경로를 입력하여 불러온다.
zFile = zipfile.ZipFile('01_10/06.압축파일_암호_푸는_프로그램/암호1234.zip')

min_len = 1
max_len = 5

unzip_result = un_zip(passwd_string, min_len, max_len, zFile)

if unzip_result == 1:
    print(" 암호찾기에 성공하였습니다. ")
else:
    print(" 암호찾기에 실패하였습니다. ")
