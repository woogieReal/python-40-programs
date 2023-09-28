"""
여러 지역 날씨를 자동으로 검색 후 저장하는 코드 만들기
"""

import pyautogui
import time
import pyperclip
import platform

weathers = ["서울 날씨", "인천 날씨", "부산 날씨", "대구 날씨", "전주 날씨"]

addr_x = 1145 # 웹 브라우저의 주소창의 좌표 x 의 값
addr_y = 100 # 웹 브라우저의 주소창의 좌표 y 의 값

# 스크린 캡처를 위한 좌표값
start_x = 700
start_y = 240
end_x = 1000
end_y = 710

def check_mac():
    return platform.system() == "Darwin"

# mac 은 화소 대비 픽셀 수가 2배라 처리 필요
coordinates = tuple([start_x * 2, start_y * 2, end_x * 2, end_y * 2]) if check_mac() else tuple([start_x, start_y, end_x, end_y])

for weather in weathers:
    pyautogui.moveTo(addr_x, addr_y, 0.1)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.write("www.naver.com", interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)
    
    pyperclip.copy(weather)
    pyautogui.hotkey("command", "v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    file_path = f"01_10/10.오토마우스를_활용한_웹페이지_자동화/{weather}.png"
    pyautogui.screenshot(file_path, region=coordinates)
    