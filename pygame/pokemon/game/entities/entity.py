import pygame

from settings import *
from game.entities.default_entity import DefaultEntity

class Entity(DefaultEntity):
    def __init__(self, x, y, solid):
        DefaultEntity.__init__(self, x, y, solid)
        self.old_surface = self.image.copy()
        self.parent = None
        self.child = None

    def start(self, tmap, surface, dest):
        self.show(surface, dest)
        if self.child is not None:
            self.child.start(tmap, self.image, (0, 0))

    def show(self, surface, dest):
        surface.blit(self.image, dest)

    def update_surface(self):
        self.child = None
        self.image.blit(self.old_surface, (0, 0))

    def add_child(self, child):
        self.old_surface = self.image.copy()
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
        return (self.x, self.y)