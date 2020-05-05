import pygame
from pygame.locals import *

from settings import *
from game.entities.default_entity import DefaultEntity
from game.map.camera import Camera

vector = pygame.math.Vector2

class Player(DefaultEntity):
    def __init__(self, game, x, y, health, speed):
        DefaultEntity.__init__(self, x, y, True, health=health, speed=speed)
        self.game = game
        self.image.fill((255, 0, 0))
        self.camera = Camera(game.surface)
        self.dir = {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
        self.ismov = False

    def update(self):
        self.camera.show(self.game.map)
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and not self.ismov:
            self.dir["RIGHT"] = 1
            self.ismov = True
        if keys[K_LEFT] and not self.ismov:
            self.dir["LEFT"] = 1
            self.ismov = True
        if keys[K_DOWN] and not self.ismov:
            self.dir["DOWN"] = 1
            self.ismov = True
        if keys[K_UP] and not self.ismov:
            self.dir["UP"] = 1
            self.ismov = True
        is_up = self.dir["UP"] and not self.game.map.has_collision(self.x, self.y-1)
        is_down = self.dir["DOWN"] and not self.game.map.has_collision(self.x, self.y+1)
        is_left = self.dir["LEFT"] and not self.game.map.has_collision(self.x-1, self.y)
        is_right = self.dir["RIGHT"] and not self.game.map.has_collision(self.x+1, self.y)
        if is_up:
            self.camera.dy -= self.speed
        if is_down:
            self.camera.dy += self.speed
        if is_left:
            self.camera.dx -= self.speed
        if is_right:
            self.camera.dx += self.speed
        if self.camera.dx % TILE_SIZE == 0 and self.camera.dy % TILE_SIZE == 0:
            if is_up:
                self.y -= 1
            if is_down:
                self.y += 1
            if is_left:
                self.x -= 1
            if is_right:
                self.x += 1
            self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
            self.ismov = False