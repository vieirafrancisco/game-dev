import os
import random

import pygame

from settings import *
from game.map.spritesheet import SpriteSheet

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.surface = pygame.Surface((self.rows * TILE_SIZE, self.cols * TILE_SIZE))
        self.src_img, self.tiles = SpriteSheet("32x32_map_tile_v4.png").get_objects()

    def show(self, master):
        for j in range(self.rows):
            for i in range(self.cols):
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                self.surface.blit(self.src_img, dest, self.tiles["grass"].rect)
        master.blit(self.surface, (0,0))


class RandomMap(Map):
    def __init__(self, rows, cols):
        Map.__init__(self, rows, cols)
        self.rand_tiles = [[random.choice(list(self.tiles.items()))[1] for _ in range(cols)] for _ in range(rows)]

    def show(self, master):
        for j in range(self.rows):
            for i in range(self.cols):
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                self.surface.blit(self.src_img, dest, self.rand_tiles[i][j])
        master.blit(self.surface, (0,0))

