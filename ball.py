import pygame


class Ball:
    def __init__(self, pos):
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.color = "pink"

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size/2)
