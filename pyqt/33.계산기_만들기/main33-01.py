"""
QT Designer로 계산기 Widget 만들기
"""

import sys 
from PyQt6.QtWidgets import *
from PyQt6 import uic


# [계산기.ui]를 불러온다.
ui_path = "33.계산기_만들기/계산기.ui"
form_class = uic.loadUiType(ui_path)[0] 


# WindowClass를 생성합니다. form_class로 부터 상속받은 자식 클래스. form_class는 [계산기.u1]
class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__() # 부모 클래스를 초기화
        self.setupUi(self)


if __name__ == "__main__" :
    # GUI를 불러온다.
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec()