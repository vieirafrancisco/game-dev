import pygame

from settings import *

class Player:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.speed = 2
        self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
        self.ismov = False

    def show(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def move(self, m):
        keys = pygame.key.get_pressed()
        print(self.dir, self.ismov)

        if keys[pygame.K_RIGHT] and not self.ismov:
            self.dir["RIGHT"] = 1
            self.ismov = True
        if keys[pygame.K_LEFT] and not self.ismov:
            self.dir["LEFT"] = 1
            self.ismov = True
        if keys[pygame.K_DOWN] and not self.ismov:
            self.dir["DOWN"] = 1
            self.ismov = True
        if keys[pygame.K_UP] and not self.ismov:
            self.dir["UP"] = 1
            self.ismov = True

        if self.dir["UP"]:
            m.dy -= self.speed
        if self.dir["DOWN"]:
            m.dy += self.speed
        if self.dir["LEFT"]:
            m.dx -= self.speed
        if self.dir["RIGHT"]:
            m.dx += self.speed

        if m.dx % TILE_SIZE == 0 and m.dy % TILE_SIZE == 0:
            self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
            self.ismov = False