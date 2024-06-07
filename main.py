import pygame

pygame.init()

# Создаем экран
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load()

# При создании игры всегда необходимо создавать игровой цикл.
# Делаем это через while. Можно было сделать бесконечный цикл while, но из него было бы не так просто выйти.
# Поэтому мы делаем через переменную.
running = True
while running:
    pass

# Игра завершится, когда мы выйдем из цикла (он будет закончен)
pygame.quit()