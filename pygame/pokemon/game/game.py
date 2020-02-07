import pygame

from settings import *
from game.map.map import Map

class Game:
    def __init__(self):
        self.size = WIDTH, HEIGHT
        self.running = False
        self._disp_window = None

    def on_init(self):
        pygame.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokémon")
        self.map = Map(20,20)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.map.draw(self._disp_window)

    def on_loop(self):
        pass

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
        self.on_cleanup()