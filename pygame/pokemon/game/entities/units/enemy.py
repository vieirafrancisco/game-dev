import random

import pygame
from pygame.locals import *

from game.entities.units.unity import Unity
from game.utils.functions import e_dist
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

    def start(self, tmap, surface, dest):
        self.show(surface, dest)
        self.move(tmap)
        if self.child is not None:
            self.child.start(tmap, surface, dest)

    def move(self, camera):
        tmap = camera.tmap
        if self.counter % self.speed == 0:
            self.counter = 1
            x, y = curr_position = self.get_pos()
            walk_possibilities = list(zip([x, x+1, x, x-1], [y-1, y, y+1, y]))
            directions = list(filter(
                lambda wp: self.can_move(camera, wp),
                walk_possibilities))
            if len(directions) > 0:
                direction = random.choice(directions)
                self.posx, self.posy = direction
                tmap.set_entity_position(self, curr_position)
        self.counter += 1

    def can_move(self, camera, wp):
        result = all([
            not camera.tmap.has_collision(*wp),
            not camera.is_player(*wp),
            e_dist(wp, self.get_respawn_pos()) <= self.walk_range
        ])
        return result

    def get_respawn_pos(self):
        return (self.respawn_posx, self.respawn_posy)