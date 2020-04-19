import pygame

from settings import *
from game.entities.units.unity import Unity

class Player(Unity):
    def __init__(self, posx, posy, health, speed):
        Unity.__init__(self, posx, posy, health, speed, solid=False)
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
        self.ismov = False
        
    def show(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def move(self, camera):
        keys = pygame.key.get_pressed()
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
        is_up = self.dir["UP"] and not camera.tmap.has_collision(self.posx, self.posy-1)
        is_down = self.dir["DOWN"] and not camera.tmap.has_collision(self.posx, self.posy+1)
        is_left = self.dir["LEFT"] and not camera.tmap.has_collision(self.posx-1, self.posy)
        is_right = self.dir["RIGHT"] and not camera.tmap.has_collision(self.posx+1, self.posy)
        if is_up:
            camera.dy -= self.speed
        if is_down:
            camera.dy += self.speed
        if is_left:
            camera.dx -= self.speed
        if is_right:
            camera.dx += self.speed
        if camera.dx % TILE_SIZE == 0 and camera.dy % TILE_SIZE == 0:
            old_pos = self.posx, self.posy
            if is_up:
                self.posy -= 1
            if is_down:
                self.posy += 1
            if is_left:
                self.posx -= 1
            if is_right:
                self.posx += 1
            self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
            self.ismov = False