"""
PC카카오톡에서 내 사진 캠처 후 저장
"""

import pyautogui
import os

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
# pyautogui가 한글을 인식하지 못함
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.png', confidence=0.5, grayscale=True)
print(picPosition)

# 앞에 사진에서 좌표를 찾지 못했다면 pic2.png 파일과 동일한 그림을 찾아 좌표를 출력
if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic2.png', confidence=0.5, grayscale=True)
    print(picPosition)

# 앞에 사진에서 좌표를 찾지 못했다면 pic3.png 파일과 동일한 그림을 찾아 좌표를 출력
if  picPosition is None:
    picPosition = pyautogui.locateOnScreen('pic3.png', confidence=0.5, grayscale=True)
    print(picPosition)