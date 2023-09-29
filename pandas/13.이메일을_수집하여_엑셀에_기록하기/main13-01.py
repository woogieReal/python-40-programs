"""
이메일 형식을 추출하는 코드 만들기
"""

import re

test_string = """
aaa@bbb.com
123@abc.co.kr
test@hello.kr
ok@ok.co.kr
ok@ok.co.kr
ok@ok.co.kr
no.co.kr
no.kr
"""

# 문자열에서 이메일 형식을 찾아 리스트형태로 결과를 반환
results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string) 

print(results)