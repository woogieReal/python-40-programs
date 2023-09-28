import random

random_number = random.randint(1, 100)

# print(random_number)

game_count = 1

# while의 조건이 True이기 때문에 break를 만나기 전까지 계속 반복
while True:
  try:
    my_number = int(input("1~100 사이의 숫자를 입력하세요:"))

    if my_number > random_number:
        print("다운")
    elif my_number < random_number:
        print("업")
    elif my_number == random_number:
        print(f"축하합니다.{game_count}회 만에 맞췄습니다.")
        break

    game_count += 1
  except:
    print("에러가 발생하였습니다.")