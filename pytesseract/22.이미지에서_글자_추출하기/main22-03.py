"""
변환된 언어를 파일로 저장하는 코드 만들기
"""

from PIL import Image
import pytesseract
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

image_path = '한글이미지.png'

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.2_1/bin/tesseract'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor+eng")

print(text)

with open('한글변환.txt', 'w', encoding="utf8") as f:
    f.write(text)