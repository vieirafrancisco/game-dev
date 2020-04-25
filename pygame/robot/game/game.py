import os
import math

import pygame
from pygame.locals import *

from settings import *
from game.entities.player import Player

def round_to(n):
    if n < 0:
        return math.floor(n)
    return math.ceil(n)

class Game:
    def __init__(self):
        self._surface = None
        self._running = False
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._running = True
        self._surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = Player(WIDTH//2,HEIGHT//2, 32, 32)
        self.circle_attr = [self._surface, (255,255,255),(20, 20), 8]
        self.circle_move = False

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.player.show(self._surface)
        pygame.draw.circle(*self.circle_attr)

    def on_loop(self):
        pygame.display.set_caption(f"Robot - FPS: {round(self.clock.get_fps(), 1)}")
        self.player.update()
        if pygame.mouse.get_pressed()[0]:
            self.circle_move = True
        if self.circle_move:
            cx, cy = self.circle_attr[2]
            mx, my = pygame.mouse.get_pos()
            ratio = 0.1
            dx, dy = round_to((mx - cx) * ratio), round_to((my - cy) * ratio)
            x, y = (cx + dx, cy + dy)
            print(x, y, cx, cy, dx, dy)
            self.circle_attr[2] = (x, y)
            if x >= cx and y >= cy:
                self.circle_move = False

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_execute(self):
        self.on_init()
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self._surface.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            self.clock.tick(60)
        self.on_cleanup()