import os
import pygame

from settings import *
from game.map.map import Map, RandomMap, LoaderMap, PixeledMap
from game.entities.player import Player
from game.entities.enemy import Enemy

class Game:
    def __init__(self):
        self.size = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokémon")
        self.map = PixeledMap(os.path.join("game","resources", "img", "maps", "map05.png"))
        self.player = Player(T_WIDTH//2, T_HEIGHT//2)
        self.enemy = Enemy(10, 9, False, walk_range=3)
        self.enemy2 = Enemy(2, 8, False, walk_range=3)
        self.enemy3 = Enemy(13, 3, False, walk_range=3)
        self.map.add_entity(self.player)
        self.map.add_entity(self.enemy)
        self.map.add_entity(self.enemy2)
        self.map.add_entity(self.enemy3)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.map.show(self._disp_window)
        self.player.show(self._disp_window)

    def on_loop(self):
        self.player.move(self.map)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_execute(self):
        self.on_init()
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self._disp_window.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
            self.clock.tick(60)
        self.on_cleanup()