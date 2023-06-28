"""
음성인식 -> 음성실행 -> 음성저장 -> 메시지 전송
ex) '안녕하세요' -> 부재중 메시지 실행 ('잠시만 기다려주세요') -> 녹음 -> 슬랙 메시지 전송
"""

import speech_recognition as sr
import pyaudio
import wave
from playsound import playsound
import os
from datetime import datetime
import requests
import json
import telegram
from dotenv import load_dotenv


load_dotenv()
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# 녹음
def record():
    # 녹음파일의 형식등을 지정
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = f"record_{datetime.today().strftime('%Y-%m-%d_%H:%M:%S')}.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("음성녹음을 시작합니다.")

    # 음성을 녹음
    frames = []

    # 44100 / 1024 * 5 = 215
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        # def read(self, num_frames, exception_on_overflow=True): Read samples from the stream.
        # 음성 스트림에서 1024 프레임으로 읽어들여 샘플을 획득
        data = stream.read(CHUNK)
        
        # 읽은 샘플을 변수에 추가
        frames.append(data)

    print("음성녹음을 완료하였습니다.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # 녹음된 음성을 저장
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


# 텔레그램 메시지 전송
def sendTelegram():
    token = os.environ.get('TELEGRAM_TOKEN')
    id = os.environ.get('TELEGRAM_CHAT_ID')

    bot = telegram.Bot(token)
    bot.sendMessage(chat_id=id, text="당신을 부르고 있습니다.")


# 슬랙 메시지 전송
def sendSlackWebhook():
    print("슬랙 메시지를 전송합니다.")
    slack_webhook_url = "https://hooks.slack.com/services/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"

    headers = { "Content-type": "application/json" }

    data = { "text": "당신을 부르고 있습니다." }

    res = requests.post(slack_webhook_url, headers=headers, data=json.dumps(data))
    print(res)

    if res.status_code == 200:
        return "ok"
    else:
        return "error"


# 음성 인식
OOO_REPLY_FILENAME = "out_of_office_message.wav"

try:
    while True :
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("음성을 입력하세요.")
            audio = r.listen(source, phrase_time_limit=5)
        try:
            stt = r.recognize_google(audio, language='ko-KR')
            if "안녕" in stt:
                record()
                playsound(OOO_REPLY_FILENAME)
                # sendSlackWebhook()
                sendTelegram()
                
            
        except sr.UnknownValueError:
            print("오디오를 이해할수 없습니다.")
        except sr.RequestError as e:
            print(f"에러가 발생하였습니다. 에러원인: {e}")

except KeyboardInterrupt:
    pass

