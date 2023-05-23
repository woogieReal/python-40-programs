"""
일정 간격마다 보내는 코드 만들기
"""

import pyautogui
import pyperclip
import time
import schedule
import os
import collections

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def send_mesaage():
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

schedule.every(10).seconds.do(send_mesaage)

while True:
    schedule.run_pending()
    time.sleep(1)