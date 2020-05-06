import os

import pygame
from pygame.locals import *

from settings import *
from game.entities.default_entity import DefaultEntity
from game.map.camera import Camera
from game.graphics.spritesheet import Spritesheet

vector = pygame.math.Vector2

def load_image(path, file_name):
    image = pygame.image.load(os.path.join(path, file_name))
    return image.convert()

class Player(DefaultEntity):
    def __init__(self, game, x, y, health, speed):
        DefaultEntity.__init__(self, x, y, True, shape=(64, 64), has_color=False, health=health, speed=speed)
        self.game = game
        self.spritesheet = Spritesheet("character", "player_tiles")
        self.spritesheet.image.set_colorkey(PINK_BACKGROUD_COLORKEY)
        self.image = self.spritesheet.get_tile_image_by_position(64, 0, 64, 64)
        self.rect.center = (x * TILE_SIZE, y * TILE_SIZE)
        self.camera = Camera(game.surface)
        self.sprite_images = {}
        self.load_sprites()
        self.dir = {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
        self.ismov = False

    def load_sprites(self):
        self.sprite_images["DOWN"] = self.spritesheet.get_tile_image_by_position(64, 0, 64, 64)
        self.sprite_images["UP"] = self.spritesheet.get_tile_image_by_position(128, 0, 64, 64)
        self.sprite_images["RIGHT"] = self.spritesheet.get_tile_image_by_position(0, 64, 64, 64)
        self.sprite_images["LEFT"] = self.spritesheet.get_tile_image_by_position(64, 64, 64, 64)

    def update(self):
        self.camera.show(self.game.map)
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT] and not self.ismov:
            self.dir["RIGHT"] = 1
            self.ismov = True
            self.image = self.sprite_images["RIGHT"]
        if keys[K_LEFT] and not self.ismov:
            self.dir["LEFT"] = 1
            self.ismov = True
            self.image = self.sprite_images["LEFT"]
        if keys[K_DOWN] and not self.ismov:
            self.dir["DOWN"] = 1
            self.ismov = True
            self.image = self.sprite_images["DOWN"]
        if keys[K_UP] and not self.ismov:
            self.dir["UP"] = 1
            self.ismov = True
            self.image = self.sprite_images["UP"]
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