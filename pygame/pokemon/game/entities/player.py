import pygame

from settings import *

class Player:
    def __init__(self, posx, posy, map):
        self.posx = posx
        self.posy = posy
        self.map = map
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def show(self):
        pygame.draw.rect(self.map.surface, (255,0,0), self.rect)

    def move(self):
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and (self.posy - 1) * TILE_SIZE >= 0:
            self.posy -= 1
        if keys[pygame.K_DOWN] and (self.posy + 1) * TILE_SIZE < HEIGHT:
            self.posy += 1
        if keys[pygame.K_LEFT] and (self.posx - 1) * TILE_SIZE >= 0:
            self.posx -= 1
        if keys[pygame.K_RIGHT] and (self.posx + 1) * TILE_SIZE < WIDTH:
            self.posx += 1
        self.rect.x = self.posx * TILE_SIZE
        self.rect.y = self.posy * TILE_SIZE
        '''
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.map.dy -= 1
        if keys[pygame.K_DOWN]:
            self.map.dy += 1
        if keys[pygame.K_LEFT]:
            self.map.dx -= 1
        if keys[pygame.K_RIGHT]:
            self.map.dx += 1