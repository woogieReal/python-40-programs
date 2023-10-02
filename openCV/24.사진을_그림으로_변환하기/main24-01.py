"""
여행사진을 그림으로 변환하는 코드 만들기
"""

import numpy as no
import cv2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# OpenCV에서 한글경로의 파일을 읽지 못해 numpy로 파일을 읽어온다.
ff = no.fromfile('샘플사진.jpg', no.uint8)

# imdecode를 하여 numpy의 이미지 파일을 OpenCV 이미지로 불러온다.
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# sigma_s 값과 sigma_r 값을 조절하여 이미지를 그림화한다.
cartoon_img = cv2.stylization(img, sigma_s=100, sigma_r=0.1)

cv2.imshow('cartoon view', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()