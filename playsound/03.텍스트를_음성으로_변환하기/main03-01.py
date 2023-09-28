"""
텍스트를 음성으로 변환하는 코드 만들기
"""

from gtts import gTTS # gtts 라이브러리 안에 gTTs 기능만 불러와 사용

str = '안녕하세요. 파이썬과 40개의 작품들 입니다.'

# 문자열을 ko(한글)로 변환하여 tts 변수에 바인딩한다.
tts = gTTS(text=str, lang='ko')

# 지정한 폴더에 hi.mp3의 파일이름으로 저장
tts.save(r'01_10/03.텍스트를_음성으로_변환하기/hi.mp3')