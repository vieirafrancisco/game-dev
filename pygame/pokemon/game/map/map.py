import os
import random

import pygame

from settings import *
from game.graphics.spritesheet import SpriteSheet
from game.entities.units.unity import Unity
from game.entities.objects.ground import Ground
from game.utils.functions import e_dist

class Map:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.surface = pygame.Surface((WIDTH, HEIGHT))
        self.src_img, self.tiles = SpriteSheet("32x32_map_tile_v4.png").get_objects()

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

    def is_instance_of(self, x, y, cls_ref):
        entity = self.get_entity(x, y)
        if entity is not None:
            return isinstance(entity, cls_ref)
        return False

    def is_solid(self, x, y):
        entity = self.get_entity(x, y)
        if entity is not None:
            return entity.solid
        return False

    def is_out_of_map(self, x, y):
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return True
        else:
            return False

    def has_collision(self, x, y):
        result = any([
            self.is_instance_of(x, y, Unity),
            self.is_solid(x, y),
            self.is_out_of_map(x, y)
        ])
        return result

    def similarity(self, rgba):
        best_tile = None
        m = INF
        for tile, obj in self.tiles.items():
            dist = e_dist(rgba, obj.rgba)
            if dist < m:
                m = dist
                best_tile = obj
        return best_tile