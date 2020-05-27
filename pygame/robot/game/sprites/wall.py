import pygame

from settings import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        groups = (game.sprites)
        pygame.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)