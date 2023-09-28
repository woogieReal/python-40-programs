"""
음성변환으로 생성되는 .mp3 파일을 파이썬에서 바로 실행하는 코드 만들기
"""

from gtts import gTTS # gtts 라이브러리 안에 gTTs 기능만 불러와 사용
from playsound import playsound
import os

# 경로를 .py파일의 실행경로로 이동, playsound에서 한글을 인식하지 못하기 때문
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# os.path.abspath(__file__)
# -> /Users/woogie/Desktop/real/python-40-programs/01_10/03.텍스트를_음성으로_변환하기/main03-02.py

# os.path.dirname(os.path.abspath(__file__))
# -> /Users/woogie/Desktop/real/python-40-programs/01_10/03.텍스트를_음성으로_변환하기

str = '안녕하세요. 파이썬과 40개의 작품들 입니다.'

tts = gTTS(text=str, lang='ko')
tts.save('hi.mp3')

playsound('hi.mp3')