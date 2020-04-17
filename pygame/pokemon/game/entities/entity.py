from abc import ABC, abstractmethod

import pygame

from settings import *

class Entity(ABC):
    def __init__(self, posx, posy, solid=False):
        self.posx = posx
        self.posy = posy
        self.solid = solid
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.old_surface = self.surface.copy()
        self.parent = None
        self.child = None

    def start(self, camera, surface, dest):
        self.show(surface, dest)
        if self.child is not None:
            self.child.start(camera, self.surface, (0, 0))

    def show(self, surface, dest):
        surface.blit(self.surface, dest)

    def update_surface(self):
        self.child = None
        self.surface.blit(self.old_surface, (0, 0))

    def add_child(self, child):
        self.old_surface = self.surface.copy()
        if self.child:
            self.child.add_child(child)
        else:
            child.parent = self
            self.child = child

    def get_top(self):
        if self.child is None:
            return self
        else:
            return self.child.get_top()

    def get_pos(self):
        return (self.posx, self.posy)