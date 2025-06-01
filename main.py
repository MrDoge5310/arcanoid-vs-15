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

enemies = list()
for x in range(45, screen.get_width() - 50, 55):
    for y in range(50, 151, 50):
        enemies.append(Enemy(x, y))

platform = Platform(1280/2, 720 - 100)
ball = Ball((1280/2, 500))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    platform.move(screen)
    platform.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)
        if enemy.check_collision(ball):
            if enemy.health <= 0:
                enemies.remove(enemy)

    ball.draw(screen)
    ball.move(screen, platform)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(FPS)  # limits FPS to 60

pygame.quit()