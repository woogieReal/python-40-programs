"""
tkinter를 사용하여 GUI 코드 만들기
"""

import tkinter

# window 객체 생성
window = tkinter.Tk()

# 타이틀을 정의
window.title("가상화폐 금액표시")

# GUI의 사이즈를 설정
window.geometry("400x200")

# 가로세로의 크기를 조절하지 못하도록 설정
window.resizable(False, False)

# hello의 문자열을 출력
label = tkinter.Label(window, text="hello")
label.pack()

# GUI를 계속 실행하기 위해 mainloop를 살행
window.mainloop()