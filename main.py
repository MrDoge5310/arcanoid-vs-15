# Example file showing a basic pygame "game loop"
import pygame
from platform import *
from ball import *
from enemy import *

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

FPS = 60

font = pygame.font.SysFont(None, 72)

# Инициализация врагов
enemies = list()
for x in range(45, screen.get_width() - 50, 55):
    for y in range(50, 201, 50):
        enemies.append(Enemy(x, y))

platform = Platform(1280 / 2, 720 - 100)
ball = Ball((1280 / 2, 500))

game_over = False
win = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Если игра окончена — отображаем сообщение и ждем выхода
    if game_over:
        screen.fill("black")
        if win:
            msg = font.render("You Win!", True, (0, 255, 0))
        else:
            msg = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(msg, (screen.get_width() // 2 - msg.get_width() // 2,
                          screen.get_height() // 2 - msg.get_height() // 2))
        pygame.display.flip()
        continue  # пропускаем обновление игрового состояния

    screen.fill("purple")

    platform.move(screen)
    platform.draw(screen)

    # Отрисовка и проверка врагов
    for enemy in enemies[:]:  # копия списка для безопасного удаления
        enemy.draw(screen)
        if enemy.check_collision(ball):
            ball.reflect(enemy)
            if enemy.health <= 0:
                enemies.remove(enemy)

    # Победа — если врагов больше нет
    if not enemies:
        game_over = True
        win = True
        continue

    # Обновление и отрисовка мяча
    ball.draw(screen)
    ball.move(screen, platform)

    # Проверка на проигрыш
    if ball.rect.top > screen.get_height():
        game_over = True
        win = False
        continue

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
