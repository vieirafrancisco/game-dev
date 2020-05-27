import pygame
from pygame.locals import *

from settings import *

class Game:
    def __init__(self):
        self._surface = None
        self._running = False
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._running = True
        self._surface = pygame.display.set_mode((WIDTH, HEIGHT))
        
    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        pass

    def on_loop(self):
        pygame.display.set_caption(f"Robot - FPS: {round(self.clock.get_fps(), 1)}")
        
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