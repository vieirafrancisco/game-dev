import pygame

from settings import *

class Tile:
    def __init__(self, pos, shape=(32,32), rgba=None ,solid=False):
        self.pos = self.x, self.y = pos
        self.shape = shape
        self.rgba = rgba
        self.solid = solid
        self.rect = pygame.Rect(self.x * shape[0], self.y * shape[1], *shape)
    
    def __str__(self):
        return f"Tile: {self.rect}"