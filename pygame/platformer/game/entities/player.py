import pygame
from pygame.locals import *

from settings import *

class Player:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.gravity = 9.8
        self.speed = 10
        self.lift = 20

    def show(self, surface):
        pygame.draw.rect(surface, (255,255,255), self.rect)

    def update(self, other):
        keys = pygame.key.get_pressed()
        if self.rect.y > HEIGHT:
            self.rect.y = 0
        if not self.rect.colliderect(other):
            self.rect.y += self.gravity

        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_UP]:
            self.rect.y -= self.lift
        if keys[K_DOWN]:
            pass