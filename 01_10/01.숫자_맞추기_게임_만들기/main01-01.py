"""
1부터 100까지의 임의의 수를 생성하고 임의의 수를 맞추는 게임 프로그램
숫자를 하나 입력하면 임의로 생성된 수보다 높은지 낮은지 정답인지 알려준다.
정담을 맞힌 경우 정답을 몇 번 만에 맞추었는지 그 결과로 게임의 승부를 알 수 있다.
"""

import random

random_number = random.randint(1, 100)

print(random_number)
# -> 1~100 사이의 정수값을 반환