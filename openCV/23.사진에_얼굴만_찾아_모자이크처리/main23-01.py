"""
OpenCV로 얼굴 사진 찾는 코드 만들기
"""

import numpy as no
import cv2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 얼굴과 눈을 찾기 위한 OpenCV 알고리즘이 적용된 파일을 불러온다.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# OpenCV에서 한글경로의 파일을 읽지 못해 numpy로 파일을 읽어온다.
ff = no.fromfile('샘플사진.jpg', no.uint8)

# imdecode를 하여 numpy의 이미지 파일을 OpenCV 이미지로 불러온다.
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)

# 이미지의 크기를 조절한다.
# fx, fy의 비율로 조절이 가능, 코드에서는 원래 비율을 사용
img = cv2.resize(img, dsize=(0, 0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴을 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러 개의 얼굴을 찾는다.
# 1.2는 ScaleFactor, 5는 minNeighbor을 나타낸다.
# ScaleFactor는 감도, minNeighbor은 최소 이격 거리
faces = face_cascade.detectMultiScale(gray, 1.2,5)

# 얼굴을 찾아 파란색으로 네모 표시를 한다.
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    
    # 눈을 찾아 녹색 네모 표시를 한다.
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh),(0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()