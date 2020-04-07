import random

import pygame
from pygame.locals import *

from game.entities.units.unity import Unity
from game.utils.functions import euclidian_distance
from settings import *

class Enemy(Unity):
    def __init__(self, posx, posy, rage, health, speed, walk_range=5, solid=True):
        Unity.__init__(self, posx, posy, health, speed, solid)
        self.respawn_posx = posx
        self.respawn_posy = posy
        self.rage = rage
        self.walk_range = walk_range
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.counter = 0

    def move(self, tmap):
        if self.counter % self.speed == 0:
            self.counter = 1
            directions = []
            for idx, (dx, dy) in enumerate(zip([0, 1, 0, -1], [-1, 0, 1, 0])):
                x, y = (self.posx + dx, self.posy + dy)
                entity = tmap.get_entity(x, y)
                if entity:
                    is_solid_entity = entity.solid
                else:
                    is_solid_entity = False
                out_of_map = x < 0 or x >= tmap.cols or y < 0 or y >= tmap.rows
                distance = euclidian_distance(x, y, self.respawn_posx, self.respawn_posy)
                if not isinstance(entity, Unity) and not is_solid_entity and distance <= self.walk_range and not out_of_map:
                    directions.append(idx)
            if directions != []:
                direction = random.choice(directions)
                x = self.posx
                y = self.posy
                if direction == UP:
                    y -= 1
                elif direction == RIGHT:
                    x += 1
                elif direction == DOWN:
                    y += 1
                elif direction == LEFT:
                    x -= 1
                old_pos = (self.posx, self.posy)
                self.posx = x
                self.posy = y
                tmap.set_entity_position(self, old_pos)
        self.counter += 1

    def get_respawn_pos(self):
        return (self.respawn_posx, self.respawn_posy)