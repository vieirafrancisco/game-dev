import random

import pygame
from pygame.locals import *

from game.entities.entity import Entity
from settings import *

class Enemy(Entity):
    def __init__(self, posx, posy, rage, walk_range=5):
        Entity.__init__(self, posx, posy)
        self.rage = rage
        self.walk_range = walk_range
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def show(self, surface):
        pygame.draw.rect(surface, (0,0,255), self.rect)

    def move(self, tmap):
        x = self.posx
        y = self.posy
        tmap.surface.blit(self.surface, ((x * TILE_SIZE) - tmap.dx, (y * TILE_SIZE) - tmap.dy))