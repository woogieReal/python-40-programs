"""
음성을 텍스트로 변환하는 코드 만들기

주의: 구글 음성변환은 API키 없이 사용시 하루 50회 제한이 있다.
"""

import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        
        # 마이크에서 음성을 받는다.
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            # 1초 후 시작하여 3초간 음성을 녹음
            audio = r.listen(source, phrase_time_limit=5)
        try:
            # 한국어 음성을 인식하여 변환
            print("음성변환: " + r.recognize_google(audio, language='ko-KR'))
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass