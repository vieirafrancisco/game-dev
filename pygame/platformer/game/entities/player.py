import pygame
from pygame.locals import *

from settings import *

vector = pygame.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = vector(x, y)
        self.vel = vector(0, 0)
        self.acc = vector(0, 0)

    def update(self):
        if self.pos.x > WIDTH + self.rect.w//2:
            self.pos.x = 0
        if self.pos.x < 0 - self.rect.w//2:
            self.pos.x = WIDTH
        if abs(self.vel.x) < 0.001:
            self.vel.x = 0
        # gravity
        if self.pos.y + self.rect.h//2 >= HEIGHT:
            self.acc = vector(0, 0)
            self.vel.y = 0
        else:
            self.acc = vector(0, 0.5)
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.acc.x -= 0.5
        if keys[K_RIGHT]:
            self.acc.x += 0.5
        # friction
        self.acc.x += self.vel.x * -0.08
        self.vel += self.acc
        # motion
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos