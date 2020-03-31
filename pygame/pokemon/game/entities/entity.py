from abc import ABC, abstractmethod

import pygame

from settings import *

class Entity(ABC):
    def __init__(self, posx, posy, solid=False):
        self.posx = posx
        self.posy = posy
        self.solid = solid
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def get_pos(self):
        return (self.posx, self.posy)