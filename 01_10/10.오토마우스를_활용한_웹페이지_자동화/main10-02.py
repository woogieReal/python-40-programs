"""
네이버에서 자동으로 서울 날씨 검색하는 코드 만들기
"""

import pyautogui
import time
import pyperclip

pyautogui.moveTo(1241, 180, 0.2)
pyautogui.click()
time.sleep(0.5)

pyperclip.copy("서울 날씨")
pyautogui.hotkey("command", "v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)