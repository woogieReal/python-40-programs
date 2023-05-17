"""
번역 내용을 새 파일로 저장하는 코드 만들기
"""

from os import linesep
import googletrans

translator = googletrans.Translator()

# 파일을 읽어올 경로를 지정
read_file_path = "01_10/09.영어_문서를_한글로_자동번역/영어파일.txt"
write_file_path = "01_10/09.영어_문서를_한글로_자동번역/한글파일.txt"

# 파일에서 줄별로 읽어 리스트 형태로 바인딩
with open(read_file_path, 'r') as f:
    readLines = f.readlines()

for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='UTF8') as f:
        f.write(result1.text + '\n')