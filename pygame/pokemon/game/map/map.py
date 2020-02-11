import os
import random

import pygame

from settings import *
from game.map.spritesheet import SpriteSheet
from game.map.utils.functions import euclidian_distance

class Map:
    def __init__(self, rows, cols):
        self.rows = max(rows, T_HEIGHT) 
        self.cols = max(cols, T_WIDTH)
        self.surface = pygame.Surface((self.cols * TILE_SIZE, self.rows * TILE_SIZE))
        self.src_img, self.tiles = SpriteSheet("32x32_map_tile_v4.png").get_objects()
        self.dx = 0
        self.dy = 0

    def show(self, master):
        for j in range(self.rows):
            for i in range(self.cols):
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                self.surface.blit(self.src_img, dest, self.tiles["grass"].rect)
        master.blit(self.surface, (0,0))


class RandomMap(Map):
    def __init__(self, rows, cols):
        Map.__init__(self, rows, cols)
        self.rand_tiles = [[random.choice(list(self.tiles.items()))[1] for _ in range(self.rows)] for _ in range(self.cols)]

    def show(self, master):
        w = WIDTH // TILE_SIZE
        h = HEIGHT // TILE_SIZE
        for j in range(h):
            y = (j + self.dy)
            for i in range(w):
                x = (i + self.dx)
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                if x < 0 or y < 0 or x > self.cols or y > self.rows :
                    tile = self.tiles["water"].rect
                else:
                    tile = self.rand_tiles[x % self.cols][y % self.rows].rect
                if i==0 and j==0: print(i, j, self.dx, self.dy, x, y)
                self.surface.blit(self.src_img, dest, tile)
        master.blit(self.surface, (0,0))

class LoaderMap(Map):
    def __init__(self, image_url):
        self.img = pygame.image.load(image_url)
        Map.__init__(self, self.img.get_height(), self.img.get_width())

    def show(self, master):
        for j in range(T_HEIGHT):
            y = (j + self.dy)
            for i in range(T_WIDTH):
                x = (i + self.dx)
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                if x < 0 or y < 0 or x > self.cols or y > self.rows :
                    tile = self.tiles["water"].rect
                else:
                    rgba = tuple(self.img.get_at((x % self.cols, y % self.rows)))
                    tile_type = self.similarity(rgba)
                    tile = self.tiles[tile_type].rect
                if i==0 and j==0: print(i, j, self.dx, self.dy, x, y)
                self.surface.blit(self.src_img, dest, tile)
        master.blit(self.surface, (0,0))

    def similarity(self, rgba):
        best_tile = ''
        m = INF
        for tile, obj in self.tiles.items():
            dist = euclidian_distance(rgba, obj.rgba)
            if dist < m:
                m = dist
                best_tile = tile
        return best_tile