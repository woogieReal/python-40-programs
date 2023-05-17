"""
영어 문서를 한글로 번역하는 코드 만들기
"""

from os import linesep
import googletrans

translator = googletrans.Translator()

# 파일을 읽어올 경로를 지정
read_file_path = "01_10/09.영어_문서를_한글로_자동번역/영어파일.txt"

# 파일에서 줄별로 읽어 리스트 형태로 바인딩
with open(read_file_path, 'r') as f:
    readLines = f.readlines()

# 리스트 형태로 저장된 readLines에서 한 줄씩 한글로 변환하여 출력
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
