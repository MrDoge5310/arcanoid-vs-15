import pygame
from random import randint


class Enemy:
    def __init__(self, x, y):
        self.width = 50
        self.height = 30
        self.rect = pygame.rect.Rect(x, y, self.width, self.height)

        self.health = randint(1, 3)

    def draw(self, screen):
        color = None
        if self.health == 3:
            color = "light green"
        elif self.health == 2:
            color = "yellow"
        else:
            color = 'red'
        pygame.draw.rect(screen, color, self.rect)

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            self.health -= 1
            return True
