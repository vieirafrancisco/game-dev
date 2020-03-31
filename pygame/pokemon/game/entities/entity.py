from abc import ABC, abstractmethod

import pygame

from settings import *

class Entity(ABC):
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
        pygame.draw.rect(self.surface, (0,0,255), (0,0,TILE_SIZE, TILE_SIZE))

    def get_pos(self):
        return (self.posx, self.posy)