"""
리스트에서 중복 내용 제거하는 코드 만들기
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

results = re.findall(r'[\w\.-]+@[\w\.-]+', test_string) 

results = list(set(results))

print(results)