"""
다수의 쓰레드를 동작시키는 코드 만들고 실행
"""

import threading

# name과 value를 입력받아 value의 회수만큼 반복
def sum(name, value):
    for i in range(0, value):
        print(f"{name} : {i}")


t1 = threading.Thread(target=sum, args=('1번 쓰레드', 10))
t2 = threading.Thread(target=sum, args=('2번 쓰레드', 10))

t1.start()
t2.start()

print("Main Thread")
