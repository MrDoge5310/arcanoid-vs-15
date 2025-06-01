import random

import pygame


class Ball:
    def __init__(self, pos):
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.color = "pink"
        self.dx = 3
        self.dy = -3

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size/2)

    def move(self, screen, platform):
        self.rect.x += self.dx
        self.rect.y += self.dy

        width, height = screen.get_size()
        if self.rect.right >= width:
            self.dx = -3
        elif self.rect.x <= 0:
            self.dx = 3
        if self.rect.y <= 0:
            self.dy = 3

        if self.rect.colliderect(platform.rect):
            self.dy = -3
            self.dx = random.choice([-3, 3])


