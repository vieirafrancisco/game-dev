import os
import random

import pygame

from settings import *
from game.graphics.spritesheet import SpriteSheet
from game.entities.units.unity import Unity
from game.entities.objects.ground import Ground
from game.map.utils.functions import euclidian_distance

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.surface = pygame.Surface((WIDTH, HEIGHT))
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
        self.entities = {}
        for j in range(self.rows):
            for i in range(self.cols):
                rgba = tuple(self.img.get_at((i, j)))
                tile = self.similarity(rgba)
                g = Ground(i, j, tile.solid)
                g.surface.blit(self.src_img, (0, 0), tile)
                self.entities[(i, j)] = g

    def show(self, master):
        for j in range(T_HEIGHT):
            y = (j + self.dy)
            for i in range(T_WIDTH):
                x = (i + self.dx)
                dest = (i * TILE_SIZE, j * TILE_SIZE)
                if x < 0 or y < 0 or x >= self.cols or y >= self.rows :
                    tile = self.tiles["default"].rect
                else:
                    tile = self.memo_tiles[x % self.cols][y % self.rows].rect
                if i==0 and j==0: print(i, j, self.dx, self.dy, x, y)
                self.surface.blit(self.src_img, dest, tile)
        master.blit(self.surface, (0,0))

    def similarity(self, rgba):
        best_tile = None
        m = INF
        for tile, obj in self.tiles.items():
            dist = euclidian_distance(rgba, obj.rgba)
            if dist < m:
                m = dist
                best_tile = obj
        return best_tile

class PixeledMap(LoaderMap):
    def __init__(self, image_url):
        LoaderMap.__init__(self, image_url)

    def show(self, master):
        # corner pins
        x0 = self.dx >> 5
        x1 = (self.dx >> 5) + T_WIDTH
        y0 = self.dy >> 5
        y1 = (self.dy >> 5) + T_HEIGHT
        print(x0, x1, y0, y1)
        for j in range(y0, y1 + 1):
            y = (j * TILE_SIZE - self.dy)
            for i in range(x0, x1 + 1):
                x = (i * TILE_SIZE - self.dx)
                dest = (x, y)
                if i >= 0 and j >= 0 and i < self.cols and j < self.rows:
                    entity = self.get_entity(i, j)
                    entity.start(self, self.surface, dest)
                else:
                    self.surface.blit(self.src_img, dest, self.tiles["default"])
        master.blit(self.surface, (0,0))

    def update(self, entity):
        top_entity = entity.get_top()
        if isinstance(top_entity, Unity):
            top_entity.move(self)

    def add_entity(self, entity):
        x, y = entity.get_pos()
        if (x, y) in self.entities.keys():
            self.entities[(x, y)].add_child(entity)
        else:
            raise Exception(f"Entity position {(x, y)} doesn't exist!")
    
    def get_entity(self, x, y):
        if (x, y) in self.entities.keys():
            return self.entities[(x, y)].get_top()
        else:
            return None

    def set_entity_position(self, entity, old_pos):
        x, y = old_pos
        if (x, y) in self.entities.keys():
            entity.parent.update_surface()
            self.add_entity(entity)
        else:
            raise Exception("Entity position doesn't exist!")