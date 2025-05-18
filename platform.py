import pygame


class Platform:
    def __init__(self, x, y):
        self.width = 200
        self.height = 50
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.center = (x, y)
        self.step = 5

    def draw(self, screen):
        pygame.draw.rect(screen, "lime", self.rect, 0, 20)
        pygame.draw.rect(screen, "blue", self.rect, 5, 20)

    def move(self, screen):
        keys = pygame.key.get_pressed()
        width = screen.get_width()

        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.step
        if keys[pygame.K_RIGHT] and self.rect.topright[0] < width:
            self.rect.x += self.step
