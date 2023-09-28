"""
메인코드가 동작할 때에만 쓰레드 동작하는 코드 만들기
"""

import threading
import time

# 1초마다 "쓰레드1 동작" 출력
def thread_1():
    while True:
        print("쓰레드1 동작")
        time.sleep(1.0)


# 쓰레드 설정 및 시작
# 쓰레드를 데몬쓰레드로 설정하여 메인동작이 실행될 때만 쓰레드를 실행하도록 함
# 데몬 스레드(Deamon thread)는 일반 스레드를 보조하는 역할, 메인 스레드가 종료되면 그 즉시 종료된다.
t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

while True:
    print("메인동작")
    time.sleep(2.0)
