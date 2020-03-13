import pygame

from settings import *

class Player:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.speed = 3

    def show(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def move(self, m):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            m.dy -= self.speed
        if keys[pygame.K_DOWN]:
            m.dy += self.speed
        if keys[pygame.K_LEFT]:
            m.dx -= self.speed
        if keys[pygame.K_RIGHT]:
            m.dx += self.speed