import pygame

from settings import *

class Tile:
    def __init__(self, pos, rgba, label=None, solid=False):
        self.pos = self.x, self.y = pos
        self.rgba = rgba
        self.label = label
        self.solid = solid
        self.rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    
    def __str__(self):
        return f"Tile<{self.label}>"