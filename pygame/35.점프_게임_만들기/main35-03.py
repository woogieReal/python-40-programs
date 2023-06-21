import pygame
import sys

FPS = 60
MAX_WIDTH = 600
MAX_HEIGHT = 400

pygame.init() # 파이게임을 초기화
clock = pygame.time.Clock() # clock을 설정
screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT)) # 스크린을 설정합니다. 600 x 400 픽셀로 설정

class Player():
    # 객체를 생성할 때 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isJump = False
        self.jumpCount = 10

    # 파란색의 네모를 x, y 좌표에 40x40사이즈로 그림. 반환하는 값은 좌표와 크기
    def draw(self):
        return pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 40, 40))

    # 플레이어의 점프를 구현
    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount**2 * 0.7 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

class Enemy():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self):
        return pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 20, 40))
    
    # 화면의 오른쪽 끝에서부터 왼쪽으로 이동하는 할수
    def move(self,speed):
        self.x = self.x - speed
        if self.x <= 0:
            self.x = MAX_WIDTH

# player의 이름으로 객체를 생성. x좌표는 50 y좌표는 바닥.
# 바닥면으로 붙이기 위해 높이에서 자신의 크기만큼 빼줌. y좌표는 위부터 0
player = Player(50, MAX_HEIGHT - 40)

# enemy의 이름으로 객체를 생성. 시작위치는 오른쪽 끝
enemy = Enemy(MAX_WIDTH, MAX_HEIGHT - 40)


def main():
    # 적의 속도를 초기기로 설정
    speed = 7
    
    while True:
        # 파이게임의 이벤트를 가져온다.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # [X] 버튼을 누르면 종료
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.isJump = True # 스페이스 키를 입력받으면 점프변수를 참으로 설정
                    
        clock.tick(FPS) # FPS를 설정. 1초에 몇 프레임이 동작할지 결정.
        screen.fill((255, 255, 255)) # 화면을 흰색으로 채운다.
        
        # 플레이어를 그립니다. 반환하는 값은 좌표와 크기
        player_rect = player.draw()
        
        # 점프를 구현. player.isJump 변수가 참이어야 동작
        player.jump()
        
        # 적을 그린다. 적의 위치와 크기를 반환
        enemy_rect = enemy.draw()
        
        # 속도는 0.01씩 점점 빨리짐
        enemy.move(speed)
        speed = speed + 0.01
        
        # 플레이어와 적과 출동하면 종료
        if player_rect.colliderect(enemy_rect):
            print("충돌")
            pygame.quit()
            sys.exit()
        
        pygame.display.update()

if __name__ == '__main__':
    main()