import pygame

from settings import *

class Tile:
    def __init__(self, x, y, solid=False):
        self.x = x
        self.y = y
        self.solid = solid
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)