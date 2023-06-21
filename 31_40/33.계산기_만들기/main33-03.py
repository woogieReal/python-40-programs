import sys 
from PyQt6.QtWidgets import *
from PyQt6 import uic


# [계산기.ui]를 불러온다.
ui_path = "31_40/33.계산기_만들기/계산기.ui"
form_class = uic.loadUiType(ui_path)[0] 


# WindowClass를 생성합니다. form_class로 부터 상속받은 자식 클래스. form_class는 [계산기.u1]
class WindowClass(QMainWindow, form_class) : 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.btn_C.clicked.connect(self.btn_clicked)
        self.btn_number0.clicked.connect(self.btn_clicked)
        self.btn_number1.clicked.connect(self.btn_clicked)
        self.btn_number2.clicked.connect(self.btn_clicked)
        self.btn_number3.clicked.connect(self.btn_clicked)
        self.btn_number4.clicked.connect(self.btn_clicked)
        self.btn_number5.clicked.connect(self.btn_clicked)
        self.btn_number6.clicked.connect(self.btn_clicked)
        self.btn_number7.clicked.connect(self.btn_clicked)
        self.btn_number8.clicked.connect(self.btn_clicked)
        self.btn_number9.clicked.connect(self.btn_clicked)
        self.btn_result.clicked.connect(self.btn_clicked)
        self.btn_minus.clicked.connect(self.btn_clicked)
        self.btn_add.clicked.connect(self.btn_clicked)
        self.btn_multipy.clicked.connect(self.btn_clicked)
        self.btn_divide.clicked.connect(self.btn_clicked)

        self.le_view.setEnabled(False)
        
        # 클래스 내부의 변수를 초기화
        self.text_value = ""
        
    def btn_clicked(self):
        btn_value = self.sender().text()
        if btn_value == 'C':
            # C 버튼이 눌렸다면 le_view의 텍스트를 0으로 초기화한 후 text_value 전역변수를 빈값으로 초기화
            print("clear")
            self.le_view.setText("0")
            self.text_value = ""
        elif btn_value == '=':
            print("=")
            try:
                # eval은 문자열 수식을 계산한 값을 출력. lstrip("0")은 왼쪽의 0을 제거. ex) 001 > 1
                resultValue = eval(self.text_value.lstrip("0"))
                
                # le_view에 계산된 값을 출력
                self.le_view.setText(str(resultValue))
            except:
                self.le_view.setText("error")
        else:
            # 숫자 및 수식 값이 눌려지면 self.text_value변수에 값을 더함
            # X 버튼이 눌렸다면 계산할 수 있는 *로 변경
            if btn_value == 'X':
                btn_value = '*'
            self.text_value = self.text_value + btn_value
            print(self.text_value)
            self.le_view.setText(self.text_value)


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show() 
    app.exec()