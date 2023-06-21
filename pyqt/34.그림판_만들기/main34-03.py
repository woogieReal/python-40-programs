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

        self.canvas = QtGui.QPixmap(self.lb_canvas.width(), self.lb_canvas.height()) 
        self.canvas.fill(QtGui.QColor("white"))  
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.clicked.connect(self.btn_clicked) 
        self.btn_black.setStyleSheet('background:black')

        self.btn_red.clicked.connect(self.btn_clicked)
        self.btn_red.setStyleSheet('background:red')

        self.btn_blue.clicked.connect(self.btn_clicked)
        self.btn_blue.setStyleSheet('background:blue')

        self.btn_clear.clicked.connect(self.btn_clear_clicked) 
    
    def btn_clicked(self):
        btn_value = self.sender().objectName()
        print(btn_value)
        if btn_value == 'btn_black':
            self.brushColor = QtGui.QColor("black")
        elif btn_value == 'btn_red':
            self.brushColor = QtGui.QColor("red")
        elif btn_value == 'btn_blue':
            self.brushColor = QtGui.QColor("blue")
    
    def btn_clear_clicked(self):
        print("모두지움")
        self.canvas.fill(QtGui.QColor("white"))
        self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e):
        # painter = QtGui.QPainter(self.lb_canvas.pixmap())
        # painter.setPen(QPen(self.brushColor, 5, Qt.PenStyle.SolidLine, Qt.PenStyle.RoundCap)) 
        # painter.drawPoint(e.position())
        # painter.end()
        # self.update()
        painter = QtGui.QPainter(self.lb_canvas.pixmap())
        pen = QPen(self.brushColor)
        pen.setStyle(Qt.PenStyle.SolidLine)  # Using Qt.PenStyle.SolidLine instead of Qt.SolidLine
        pen.setWidth(5)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        painter.setPen(pen)
        painter.drawPoint(e.position())
        painter.end()
        self.update()

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec()