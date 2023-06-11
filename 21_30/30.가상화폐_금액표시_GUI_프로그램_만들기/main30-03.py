"""
1초마다 반복해서 동작하는 코드 만들기
"""

import tkinter
import tkinter.font

# window 객체 생성
window = tkinter.Tk()

# 타이틀을 정의
window.title("가상화폐 금액표시")

# GUI의 사이즈를 설정
window.geometry("400x200")

# 가로세로의 크기를 조절하지 못하도록 설정
window.resizable(False, False)



# 폰트를 적용하여 hello의 문자열을 출력
font = tkinter.font.Font(size=30)
label = tkinter.Label(window, text="hello", font=font)
label.pack()

cnt = 0

# 1초마다 실행되는 함수
def get_coin_1sec():
    # 함수 안에서 cnt의 전역변수를 사용하기 위해 global를 붙여 전역변수인 cnt를 사용
    global cnt
    now_btc_price = str(cnt)
    cnt = cnt + 1
    
    # 라벨의 text를 변경
    label.config(text=now_btc_price)
    
    # 1초 후에 get_coin_1sec 함수를 불러온다.
    window.after(1000, get_coin_1sec)

# 한 번 실행 후 자기 자신을 1초마다 호출
get_coin_1sec()

# GUI를 계속 실행하기 위해 mainloop를 살행
window.mainloop()