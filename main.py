import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Название и иконка окна
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/tir.png")
pygame.display.set_icon(icon)

# Изображение мишени
target_img = pygame.image.load("img/tir.png")
# Масштабируем изображение до нужного размера (80x80)
target_width = 80
target_height = 80
target_img = pygame.transform.scale(target_img, (target_width, target_height))
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Главный игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            print(f"Координаты мыши: ({mouse_x}, {mouse_y})")  # Отладочная информация
            # Проверка на пересечение
            if (
                target_x <= mouse_x <= target_x + target_width
                and target_y <= mouse_y <= target_y + target_height
            ):
                print("Мишень уничтожена!")
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Отрисовка
    screen.fill(color)  # Заливка экрана случайным цветом
    screen.blit(target_img, (target_x, target_y))

    # Обновление экрана
    pygame.display.update()

# Завершение Pygame
pygame.quit()