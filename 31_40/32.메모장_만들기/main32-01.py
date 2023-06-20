"""
메모장의 뼈대를 구성하고 메뉴를 구성
"""

from tkinter import *
from tkinter.filedialog import *


def new_file():
    pass

def save_file():
    pass

def maker():
    pass


"""
geometry( {w}x{h} {±x}{±y})
{w}  창의 너비
{h}  창의 높이
{±x} 창의 가로 방향 위치, + 값은 화면 왼쪽 끝에서의 거리, - 값은 화면 오른쪽 끝에서의 거리를 의미한다.
{±y} 창의 세로 방향 위치, + 값은 화면 윗쪽 끝에서의 거리, - 값은 화면 아랫쪽 끝에서의 거리를 의미한다.

tearoff [default value:1] : boolean
tearoff를 사용하면 기본 창에 대한 메뉴를 분리하여 부동 메뉴를 만들 수 있습니다.
메뉴를 만들면 상단 메뉴 항목을 클릭하면 상단에 점선이 표시됩니다.
그 점선들을 클릭하면 메뉴가 찢어져서 떠 있는 상태가 된다.
"""

window = Tk() # window 객체 생성
window.title("메모장") # 타이틀을 정의
window.geometry("400x400+800+300") # GUI의 사이즈를 설정
window.resizable(False, False) # 가로세로의 크기를 조절하지 못하도록 설정

# 첫 번째 메뉴를 구성. 새파일, 저장, 종료를 파일의 이름으로 묶는다.
menu = Menu(window)
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="새파일", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator() # 메뉴에 줄을 추가
menu_1.add_command(label="종료", command=window.destroy)
menu.add_cascade(label="파일", menu=menu_1)

# 두 번째 메뉴를 구성. 만든이를 만든이의 이름으로 묶는다.
menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="만든이", command = maker)
menu.add_cascade(label="만든이", menu=menu_2)

# 메뉴를 구성
window.config(menu=menu)

window.mainloop()