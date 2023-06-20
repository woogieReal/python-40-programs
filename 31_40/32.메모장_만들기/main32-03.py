from tkinter import *
from tkinter.filedialog import *


# 텍스트 영역을 지움
def new_file():
    """
    delete(self, index1, index2=None)
    Delete the characters between INDEX1 and INDEX2
    delete(3.0,END): 3번 째 줄 이후로 모두 삭제
    """
    text_area.delete(1.0,END)

# .txt 파일명으로 텍스트의 내용을 저장
def save_file():
    f = asksaveasfile(mode = "w", defaultextension=".txt",filetypes=[('Text files', '.txt')])
    text_save = str(text_area.get(1.0, END)) # 텍스트 창의 모든 문자열을 가져옴
    f.write(text_save)
    f.close()

# 새로운 만든이 창이 생성되고 내용이 표시된다.
def maker():
    help_view = Toplevel(window)
    help_view.geometry("300x50+800+300")
    help_view.title("만든이")
    lb = Label(help_view, text = "파이썬과 40개의 작품들 메모장 만들기 입니다.")
    lb.pack()


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

# 텍스트를 입력받을 수 있는 창을 추가
text_area = Text(window)

# 왼쪽 오른쪽 공백을 설정
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# 텍스트 창을 동서남북 방향으로 붙인다.
text_area.grid(sticky = N + E + S + W)

# 메뉴를 구성
window.config(menu=menu)

window.mainloop()