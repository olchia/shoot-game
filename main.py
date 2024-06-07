import pygame
import random

pygame.init()

# Создаем экран
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")

icon = pygame.image.load("img/512x512bb.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

colour = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


# При создании игры всегда необходимо создавать игровой цикл.
# Делаем это через while. Можно было сделать бесконечный цикл while, но из него было бы не так просто выйти.
# Поэтому мы делаем через переменную.
running = True
while running:
    pass

# Игра завершится, когда мы выйдем из цикла (он будет закончен)
pygame.quit()