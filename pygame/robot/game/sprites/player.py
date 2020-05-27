import pygame
from pygame.locals import *

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        groups = (game.sprites)
        pygame.sprite.Sprite.__init__(self, groups)
        self.game = game
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass