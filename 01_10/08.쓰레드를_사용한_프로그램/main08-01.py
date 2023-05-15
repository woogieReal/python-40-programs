"""
2가지 동작이 동시에 실행되는 코드 만들고 실행
"""

import threading
import time

# 1초마다 "쓰레드1 동작" 출력
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)


# 쓰레드 설정 및 시작
t1 = threading.Thread(target=thread_1)
t1.start()

# 메인코드로 "메인동작"을 2초마다 출력
while True:
    print("메인동작")
    time.sleep(2.0)
