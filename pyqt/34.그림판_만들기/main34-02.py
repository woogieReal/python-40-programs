import sys 
from PyQt6 import QtGui, uic
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


ui_path = "34.그림판_만들기/그림판.ui"
form_class = uic.loadUiType(ui_path)[0] 


class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.brushColor = QtGui.QColor("black")  

        # lb_canvas를 canvas으로 설정
        self.canvas = QtGui.QPixmap(self.lb_canvas.width(), self.lb_canvas.height()) 
        self.canvas.fill(QtGui.QColor("white"))  
        self.lb_canvas.setPixmap(self.canvas)

        # btn_black 버튼을 검정색으로 합니다. 버튼을 누를 때 동작하는 함수를 연결
        self.btn_black.clicked.connect(self.btn_clicked) 
        self.btn_black.setStyleSheet('background:black')

        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet('background:red')

        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet('background:blue')

        self.btn_clear.clicked.connect(self.btn_clear_clicked) 
    
    # 6. btn_black btn_red, btn_blue 버튼을 누를 때 동작하는 함수
    def btn_clicked(self):
        btn_value = self.sender().objectName()
        print(btn_value)
    
    # 모두지움 버튼을 누를 때 동작하는 함수
    def btn_clear_clicked(self):
        print("모두지움")

    # 마우스를 클릭할 때 마우스의 좌표를 출력하는 함수
    def mouseMoveEvent(self, e):
        """
        https://doc.qt.io/qtforpython-6/PySide6/QtGui/QMouseEvent.html#PySide6.QtGui.PySide6.QtGui.QMouseEvent.x
        Use position() .x() instead.
        """
        # print(e.x(),e.y())
        print(e.position())

if __name__ == "__main__" :
    # GUI를 불러온다.
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec()