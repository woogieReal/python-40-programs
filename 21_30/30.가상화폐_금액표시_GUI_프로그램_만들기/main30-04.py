"""
1초마다 반복해서 동작하는 GUI 코드 만들기
"""

import tkinter
import tkinter.font
import pyupbit
import threading
import threading
import time

coin_price = 0

# 1초마다 비트코인의 시세를 가져와 coin_price 전역변수에 저장하는 쓰레드 프로그램을 생성
# 데몬 쓰레드로 생성하여 메인 프로그램이 종료되면 함께 종료된다.
def get_coin_price():
    # 함수 안에서 coin_price의 전역변수를 사용하기 위해 global를 붙여 전역변수인 coin_price를 사용
    global coin_price
    while True:
        coin_price = pyupbit.get_current_price("KRW-BTC")
        time.sleep(1.0)

t1 = threading.Thread(target=get_coin_price)
t1.daemon = True
t1.start()

# window 객체 생성
window = tkinter.Tk()

# 타이틀을 정의
window.title("비트코인 실시간 가격")

# GUI의 사이즈를 설정
window.geometry("400x50")

# 가로세로의 크기를 조절하지 못하도록 설정
window.resizable(False, False)

# 폰트를 적용하여 텍스트 출력
font = tkinter.font.Font(size=30)
label = tkinter.Label(window, text="", font=font)
label.pack()

# 1초마다 실행되는 함수, coin_price의 가격을 1초마다 GUI에 표시
def get_coin_1sec():
    global coin_price
    now_btc_price = str(coin_price)
    
    # 라벨의 text를 변경
    label.config(text=now_btc_price)
    
    # 1초 후에 get_coin_1sec 함수를 불러온다.
    window.after(1000, get_coin_1sec)

# 한 번 실행 후 자기 자신을 1초마다 호출
get_coin_1sec()

# GUI를 계속 실행하기 위해 mainloop를 살행
window.mainloop()
