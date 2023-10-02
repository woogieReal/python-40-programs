"""
사용 가능한 언어 확인하는 코드 만들기
"""

import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.2_1/bin/tesseract'
languages = pytesseract.get_languages(config='')
print(languages)
# -> ['eng', 'kor', 'osd', 'snum']