"""
일정 시간마다 동작하는 코드 만들기
"""

import pyautogui
import pyperclip
import time
import threading
import os
import collections

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 카카오톡에 메시지를 보내는 코드
def send_mesaage():
    # send_mesaage 함수를 10초 후에 실행.
    # 자신의 함수에서 10초 후에 자신의 함수를 불러오기 때문에 10초 마다 실행된다.
    threading.Timer(10, send_mesaage).start()
    
    picPosition = pyautogui.locateOnScreen('pic1.png')
    print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic2.png')
        print(picPosition)

    if  picPosition is None:
        picPosition = pyautogui.locateOnScreen('pic3.png')
        print(picPosition)

    # 이미지에서 찾은 좌표의 중간 좌표값을 찾는다.
    clickPosition = pyautogui.center(picPosition)
    
    # 맥의 경우 화소 대비 픽셀 수가 2배라 처리 필요
    Point = collections.namedtuple("Point", 'x y')
    clickPositionForMac = Point(x=clickPosition.x/2, y=clickPosition.y/2)
    # clickPositionForMac = Point(x=1535, y=132)
    
    print(clickPosition)
    print(clickPositionForMac)

    pyautogui.click(clickPositionForMac)
    pyautogui.doubleClick(clickPositionForMac)
    
    time.sleep(1.0)

    pyperclip.copy("이 메세지는 자동으로 보내는 메세지 입니다~~") 
    pyautogui.hotkey("command", "v")
    time.sleep(1.0)

    pyautogui.write(["enter"])
    time.sleep(1.0)

    pyautogui.write(["escape"])
    time.sleep(1.0)

# 처음 한 번 send_mesaage 함수를 실행, 이후에는 threading.Timer에 의해 10초마다 불러지게 된다.
send_mesaage()