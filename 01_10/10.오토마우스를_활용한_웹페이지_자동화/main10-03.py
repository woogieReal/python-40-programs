"""
서울 날씨 화면 자동 캡처 후 저장하는 코드 만들기
"""

import pyautogui
import time
import pyperclip
import platform

pyautogui.moveTo(1241, 180, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("command", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)

start_x = 700
start_y = 240
end_x = 1000
end_y = 710

def check_mac():
    return platform.system() == "Darwin"

# mac 은 화소 대비 픽셀 수가 2배라 처리 필요
coordinates = tuple([start_x * 2, start_y * 2, end_x * 2, end_y * 2]) if check_mac() else tuple([start_x, start_y, end_x, end_y])

pyautogui.screenshot('01_10/10.오토마우스를_활용한_웹페이지_자동화/서울날씨.png', region=coordinates)