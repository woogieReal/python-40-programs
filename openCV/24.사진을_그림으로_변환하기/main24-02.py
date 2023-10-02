"""
실시간으로 sigma_s 값과 sigma_r 값의 변화에 따라 사진이 변화하는 코드 만들기
"""

import numpy as np
import cv2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# OpenCV에서 한글경로의 파일을 읽지 못해 numpy로 파일을 읽어온다.
ff = np.fromfile('샘플사진.jpg', np.uint8)

# imdecode를 하여 numpy의 이미지 파일을 OpenCV 이미지로 불러온다.
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지의 크기를 조절한다.
# fx, fy의 비율로 조절이 가능, 코드에서는 원래 비율을 사용
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

def onChange(pos):
    pass

# 트랙 윈도우를 생성
cv2.namedWindow("Trackbar Windows")

# 트랙의 최소 최대값을 설정
# 트랙이 움직일 때 마다 동작하는 함수를 지정한다.
cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

# 트랙의 기본 위치를 지정
cv2.setTrackbarPos("sigma_s", "Trackbar Windows", 100)
cv2.setTrackbarPos("sigma_r", "Trackbar Windows", 10)

# 계속 반복
while True:
    
    # openCV에서 킷값을 입력받는다.
    # 100ms 동안 킷값을 기다리다가 값이 없으면 timeout으로 아래 코드를 종료하고 다음 코드를 실행시킨다.
    # q의 킷값이 입력되면 break로 while문을 종료한다.
    if cv2.waitKey(100) == ord('q'):
        break
    
    # 트랙의 포지션으로 sigma_s_value, sigma_r_value 값을 받는다.
    # sigma_r_value 값은 나누기 100을 한다.
    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows") / 100.0

    print("sigma_s_value:",sigma_s_value)
    print("sigma_r_value:",sigma_r_value)

    # 트랙의 포지션에 따라서 이미지를 그림화한다.
    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)  

    cv2.imshow("Trackbar Windows", cartoon_img)

# openCV의 모든창이 닫히고 종료됨
cv2.destroyAllWindows() 