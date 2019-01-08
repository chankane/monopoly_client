import pygame
from pygame.locals import *
import sys  # For exit()
import settings


def has_exit():
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:  # 閉じるボタンが押されたら終了
            return True
    return False


def loop(screen):
    screen.fill((0, 0, 0))  # 画面を黒色(#000000)に塗りつぶし
    pygame.draw.rect(screen, (0, 80, 0), Rect(10, 10, 80, 50), 5)
    pygame.display.update()  # 画面を更新


def main():
    pygame.init()
    screen = pygame.display.set_mode(settings.SCREEN_SIZE)
    pygame.display.set_caption(settings.TITLE)

    while not has_exit():
        loop(screen)
        pygame.time.Clock().tick(settings.FPS)

    pygame.quit()  # Pygame の終了(画面閉じられる)
    sys.exit()


if __name__ == "__main__":
    main()
