import pygame

from settings import *
from game.map.map import Map, RandomMap
from game.entities.player import Player

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
        self.map = RandomMap(20,20)
        self.player = Player(0,0)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.map.show(self._disp_window)
        self.player.show(self._disp_window)

    def on_loop(self):
        pass

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        self.player.move()

    def on_execute(self):
        self.on_init()
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)
            self._disp_window.fill((0,0,0))
            self.on_loop()
            self.on_render()
            pygame.display.flip()
        self.on_cleanup()