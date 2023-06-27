"""
음성을 녹음하는 코드 만들기

참고
https://people.csail.mit.edu/hubert/pyaudio/docs/
"""

import pyaudio
import wave
from playsound import playsound
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

"""
format: Sampling size and format
* int
* paFloat32, paInt32, paInt24, paInt16, paInt8, paUInt8, paCustomFormat
* paInt16 = 16 bit int = int 8
  * 2^16 가지를 표현할 수 있다.
  * 보통 16비트, 무손실 음원은 24비트

channels: Number of channels
* int
* 소리가 나오는 스피커의 갯수
* 1 = 모노
* 2 = 스테레오
* ~~2.1 = 스테레오 + 우퍼~~ 사용 불가, 데이터 타입이 int

rate: Sampling rate
* int
* 1초 당 들리는 Sample의 갯수를 단위로 나타낸 것
* Sample: 오디오 신호의 작은 단위, 오디오 조각
* 보통 음악작업에서 쓰이는 Sampling Rate는 44.1kHz(=44,100Hz)
  * 44,100개의 끊어진 Audio 조각들이 1초에 담겨있다.

input: Specifies whether this is an input stream.
* bool, Default False
* 스트림은 일련의 연속성을 갖는 데이터

frames_per_buffer: Specifies the number of frames per buffer.
* int
* 버퍼: 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
* 프레임:
  * 44100Hz의 Sampling rate로 만들어진 오디오에는 초당 44100개의 프레임이 포함된다.
  * 모노인 경우에는 샘플의 갯수가 프레임과 동일
  * 스테레오인 경우에는 샘플이 프레임의 2배

* ex. 채널이 스테레오, 샘플링 레이트가 44100Hz의 오디오의 경우 초당 88200개의 샘플이 모인 44100개의 프레임으로 이루어진다.
"""

# 녹음파일의 형식등을 지정
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

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

print("녹음된 파일을 재생합니다.")

# 경로에 한글이 포함되면 오류 발생
playsound(WAVE_OUTPUT_FILENAME)