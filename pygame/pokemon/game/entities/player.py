import pygame

from settings import *
from game.entities.entity import Entity

class Player(Entity):
    def __init__(self, posx, posy):
        Entity.__init__(self, posx, posy, solid=False)
        self.rect = pygame.Rect(posx * TILE_SIZE, posy * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.speed = 2
        self.dir = {"RIGHT": 0, "LEFT": 0, "UP": 0, "DOWN": 0}
        self.ismov = False

    def show(self, surface):
        pygame.draw.rect(surface, (255,0,0), self.rect)

    def move(self, m):
        keys = pygame.key.get_pressed()
        #print(self.dir, self.ismov, self.posx, self.posy)

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

        is_up = self.dir["UP"] and not self.iscollide(m, self.posx, self.posy-1)
        is_down = self.dir["DOWN"] and not self.iscollide(m, self.posx, self.posy+1)
        is_left = self.dir["LEFT"] and not self.iscollide(m, self.posx-1, self.posy)
        is_right = self.dir["RIGHT"] and not self.iscollide(m, self.posx+1, self.posy)

        if is_up:
            m.dy -= self.speed
        if is_down:
            m.dy += self.speed
        if is_left:
            m.dx -= self.speed
        if is_right:
            m.dx += self.speed

        if m.dx % TILE_SIZE == 0 and m.dy % TILE_SIZE == 0:
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

    def iscollide(self, tmap, x, y):
        tile_is_solid = tmap.get_tile(x, y).solid
        if tmap.get_entity(x, y):
            entity_is_solid = tmap.get_entity(x, y).solid
        else:
            entity_is_solid = False
        if tile_is_solid or entity_is_solid:
            return True
        else:
            return False 