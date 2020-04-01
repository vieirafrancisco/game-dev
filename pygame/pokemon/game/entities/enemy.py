import random

import pygame
from pygame.locals import *

from game.entities.entity import Entity
from game.entities.player import Player
from game.utils.functions import euclidian_distance
from settings import *

class Enemy(Entity):
    def __init__(self, posx, posy, rage, walk_range=5, solid=True):
        Entity.__init__(self, posx, posy, solid)
        self.respawn_posx = posx
        self.respawn_posy = posy
        self.rage = rage
        self.walk_range = walk_range
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.counter = 0
        self.velocity = 50

    def show(self, surface):
        pass

    def move(self, tmap):
        if self.counter % self.velocity == 0:
            self.counter = 1
            r = random.choice([UP, RIGHT, DOWN, LEFT])
            x = self.posx
            y = self.posy
            if r == UP:
                y -= 1
            elif r == RIGHT:
                x += 1
            elif r == DOWN:
                y += 1
            elif r == LEFT:
                x -= 1
            is_solid_tile = tmap.get_tile(x, y).solid
            entity = tmap.get_entity(x, y)
            if entity:
                is_solid_entity = entity.solid
            else:
                is_solid_entity = False
            distance = euclidian_distance(x, y, self.respawn_posx, self.respawn_posy)
            if not isinstance(entity, Player) and not is_solid_tile and not is_solid_entity and distance <= self.walk_range:
                old_pos = (self.posx, self.posy)
                self.posx = x
                self.posy = y
                tmap.set_entity_position(self, old_pos)
        tmap.surface.blit(self.surface, ((self.posx * TILE_SIZE) - tmap.dx, (self.posy * TILE_SIZE) - tmap.dy))
        self.counter += 1

    def get_respawn_pos(self):
        return (self.respawn_posx, self.respawn_posy)