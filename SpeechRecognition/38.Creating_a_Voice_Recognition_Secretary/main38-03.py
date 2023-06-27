"""
특정 키워드에 답변하는 음성인식 비서 코드 만들기

참고
https://pypi.org/project/SpeechRecognition/

주의: 구글 음성변환은 API키 없이 사용시 하루 50회 제한이 있다.
"""

import speech_recognition as sr

try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source, phrase_time_limit=5)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            print("음성변환: " + stt)
            if "안녕" in stt:
                print("네 안녕하세요")
            elif "날씨" in stt:
                print("정말 날씨가 좋네요")
            
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass