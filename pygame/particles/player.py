import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x - 10, self.y - 10, 20, 20)

    def draw(self, surface):
        pygame.draw.rect(surface, (125,0,0), self.rect)