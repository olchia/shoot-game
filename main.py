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

colour = (75, 0, 130)

# Переменная для подсчета попаданий по мишени
click = 0

# При создании игры всегда необходимо создавать игровой цикл.
# Делаем это через while. Можно было сделать бесконечный цикл while, но из него было бы не так просто выйти.
# Поэтому мы делаем через переменную.
running = True
while running:
    screen.fill(colour)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                click += 1
    screen.blit(target_img, (target_x, target_y))

    # Отображение количества попаданий
    font_size = 26
    font_name = "Arial"
    font = pygame.font.SysFont(font_name, font_size)
    text = font.render(f"Количество попаданий по мишени: {click}", True, (255, 245, 238))
    screen.blit(text, (10, 10))

    pygame.display.update()

# Игра завершится, когда мы выйдем из цикла (он будет закончен)
pygame.quit()