"""
파일에서 문자를 읽어 음성으로 출력하는 코드 만들고 실행
"""

from gtts import gTTS # gtts 라이브러리 안에 gTTs 기능만 불러와 사용
from playsound import playsound
import os

# 경로를 .py파일의 실행경로로 이동, playsound에서 한글을 인식하지 못하기 때문
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt'

# 파일을 f의 이름으로 오픈한다.
# 한글로 작성된 파일을 열기 때문에 'rt', encoding='UTF8' 형식으로 열어 글자가 때지지 않게 한다.
with open(file_path, 'rt', encoding='UTF8') as f:
  read_file = f.read()

tts = gTTS(text=read_file, lang='ko')

tts.save('myText.mp3')

playsound('myText.mp3')