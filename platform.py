import pygame


class Platform:
    def __init__(self, x, y):
        self.width = 200
        self.height = 50
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.center = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, "lime", self.rect, 0, 20)
        pygame.draw.rect(screen, "blue", self.rect, 5, 20)
