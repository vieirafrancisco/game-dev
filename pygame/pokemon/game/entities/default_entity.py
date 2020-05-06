import pygame
from pygame.locals import *

from settings import *

class DefaultEntity(pygame.sprite.Sprite):
    def __init__(self, x, y, solid, shape=TILE_SHAPE, has_color=True, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.solid = solid
        self.kwargs = kwargs
        self.image = pygame.Surface(shape).convert()
        self.image.fill(DEFAULT_COLOR)
        if not has_color:
            self.image.set_colorkey(DEFAULT_COLOR)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x * TILE_SIZE, self.y * TILE_SIZE)

    def __getattr__(self, attr):
        try:
            return self.kwargs[attr]
        except Exception as e:
            raise Exception(f"Don't have a attribute with that name! Error log: {e}")