import pygame


class Ball:
    def __init__(self, pos):
        self.size = 50
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.rect.center = pos
        self.color = "pink"
        self.dx = 1
        self.dy = -1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.size/2)

    def move(self, screen):
        self.rect.x += self.dx
        self.rect.y += self.dy

        width, height = screen.get_size()
