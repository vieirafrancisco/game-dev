import pygame

from settings import *

class Player:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def show(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def move(self, m):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            m.dy -= 1
        if keys[pygame.K_DOWN]:
            m.dy += 1
        if keys[pygame.K_LEFT]:
            m.dx -= 1
        if keys[pygame.K_RIGHT]:
            m.dx += 1