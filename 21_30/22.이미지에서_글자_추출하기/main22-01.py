"""
이미지에서 한글 찾아 추출하는 코드 만들기
"""

from PIL import Image
import pytesseract

image_path = '21_30/22.이미지에서_글자_추출하기/한글이미지.png'

pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/Cellar/tesseract/5.3.1/bin/tesseract'
text = pytesseract.image_to_string(Image.open(image_path), lang="kor+eng")

print(text)