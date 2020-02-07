import os

import pygame

from settings import *
from game.map.spritesheet import SpriteSheet

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.surface = pygame.Surface((self.rows * TILE_SIZE, self.cols * TILE_SIZE))
        self.spritesheet = SpriteSheet("32x32_map_tile_v4.png")

    def draw(self, master):
        for j in range(self.rows):
            for i in range(self.cols):
                source = self.spritesheet.image
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                tiles = self.spritesheet.tiles
                self.surface.blit(source, dest, tiles["water"])
        master.blit(self.surface, (0,0))