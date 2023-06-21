"""
게임화면 구성하고 스페이스바를 입력 받는 코드 만들기
"""

import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init() # 파이게임을 초기화
clock = pygame.time.Clock() # clock을 설정
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT)) # 스크린을 설정합니다. 600 x 400 픽셀로 설정

def main():
    while True:
        # 파이게임의 이벤트를 가져온다.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # [X] 버튼을 누르면 종료
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # 키 다운 입력 중에 스페이스바가 눌리면 space를 출력
                if event.key == pygame.K_SPACE:
                    print("space")
                    
        clock.tick(FPS) # FPS를 설정. 1초에 몇 프레임이 동작할지 결정.
        screen.fill((255, 255, 255)) # 화면을 흰색으로 채운다.
        
        # 화면을 그려준다.
        pygame.display.update()

if __name__ == '__main__':
    main()