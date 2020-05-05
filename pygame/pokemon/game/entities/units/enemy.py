import random

import pygame
from pygame.locals import *

from game.entities.units.unity import Unity
from game.utils.functions import e_dist
from settings import *

class Enemy(Unity):
    def __init__(self, x, y, rage, health, speed, walk_range=5, solid=True):
        Unity.__init__(self, x, y, solid, health, speed)
        self.rage = rage
        self.walk_range = walk_range
        self.respawn_x = x
        self.respawn_y = y
        self.counter = 0

    def start(self, tmap, surface, dest):
        self.show(surface, dest)
        self.move(tmap)
        if self.child is not None:
            self.child.start(tmap, surface, dest)

    def move(self, tmap):
        if self.counter % self.speed == 0:
            self.counter = 1
            x, y = curr_position = self.get_pos()
            walk_possibilities = [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]
            directions = list(filter(
                lambda wp: self.can_move(tmap, wp),
                walk_possibilities))
            if len(directions) > 0:
                direction = random.choice(directions)
                self.x, self.y = direction
                try:
                    tmap.set_entity_position(self, curr_position)
                except Exception as e:
                    self.x, self.y = curr_position
                    print(e)
        self.counter += 1

    def can_move(self, tmap, wp):
        result = all([
            not tmap.has_collision(*wp),
            e_dist(wp, self.get_respawn_pos()) <= self.walk_range
        ])
        return result

    def get_respawn_pos(self):
        return (self.respawn_x, self.respawn_y)