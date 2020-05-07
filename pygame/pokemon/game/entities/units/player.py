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
        self.image = self.spritesheet.get_tile_image("down_stand")
        self.rect.center = (x * TILE_SIZE, y * TILE_SIZE)
        self.camera = Camera(game.surface)
        self.sprite_images = {}
        self.load_sprites()
        self.dir = {"UP": 0, "RIGHT": 0, "DOWN": 0, "LEFT": 0}
        self.ismov = False
        self.last_update = 0
        self.curr_frame = 0

    def load_sprites(self):
        # down movement images
        self.sprite_images["DOWN_STAND"] = self.spritesheet.get_tile_image("down_stand")
        self.sprite_images["DOWN"] = [
            self.spritesheet.get_tile_image("down_m1"),
            self.spritesheet.get_tile_image("down_m2")]
        # up movement images
        self.sprite_images["UP_STAND"] = self.spritesheet.get_tile_image("up_stand")
        self.sprite_images["UP"] = [
            self.spritesheet.get_tile_image("up_m1"),
            self.spritesheet.get_tile_image("up_m2")]
        # right movement images
        self.sprite_images["RIGHT_STAND"] = self.spritesheet.get_tile_image("right_stand")
        self.sprite_images["RIGHT"] = [
            self.spritesheet.get_tile_image("right_m1"),
            self.spritesheet.get_tile_image("right_m2")]
        # left movement images
        self.sprite_images["LEFT_STAND"] = self.spritesheet.get_tile_image("left_stand")
        self.sprite_images["LEFT"] = [
            pygame.transform.flip(right_image, False, False)
            for right_image in self.sprite_images["RIGHT"]]

    def animate(self, side):
        now = pygame.time.get_ticks()
        if now - self.last_update > 250:
            self.last_update = now
            self.curr_frame = (self.curr_frame + 1) % 2
            self.image = self.sprite_images[side][self.curr_frame]    

    def update(self):
        self.camera.show(self.game.map)
        keys = pygame.key.get_pressed()
        if not self.ismov:
            if keys[K_RIGHT]:
                self.image = self.sprite_images["RIGHT_STAND"]
                if not self.game.map.has_collision(self.x + 1, self.y):
                    self.ismov = True
                    self.dir["RIGHT"] = 1
                    self.x += 1
            elif keys[K_UP]:
                self.image = self.sprite_images["UP_STAND"]
                if not self.game.map.has_collision(self.x, self.y - 1):
                    self.ismov = True
                    self.dir["UP"] = 1
                    self.y -= 1
            elif keys[K_DOWN]:
                self.image = self.sprite_images["DOWN_STAND"]
                if not self.game.map.has_collision(self.x, self.y + 1):
                    self.ismov = True
                    self.dir["DOWN"] = 1
                    self.y += 1
            elif keys[K_LEFT]:
                self.image = self.sprite_images["LEFT_STAND"]
                if not self.game.map.has_collision(self.x - 1, self.y):
                    self.ismov = True
                    self.dir["LEFT"] = 1
                    self.x -= 1
        else:
            if self.dir["RIGHT"]:
                self.camera.dx += self.speed
                side = "RIGHT"
                self.animate(side)
            elif self.dir["UP"]:
                self.camera.dy -= self.speed
                side = "UP"
                self.animate(side)
            elif self.dir["DOWN"]:
                self.camera.dy += self.speed
                side = "DOWN"
                self.animate(side)
            elif self.dir["LEFT"]:
                self.camera.dx -= self.speed
                side = "LEFT"
                self.animate(side)
            if self.camera.dx % TILE_SIZE == 0 and self.camera.dy % TILE_SIZE == 0:
                self.image = self.sprite_images[f"{side}_STAND"]
                self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
                self.ismov = False