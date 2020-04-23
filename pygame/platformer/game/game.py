import pygame
from pygame.locals import *

from settings import *
from game.entities.player import Player

class Game:
    def __init__(self):
        self._surface = None
        self._running = False
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._running = True
        self._surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = Player(WIDTH//2, HEIGHT//2, 32, 32)
        self.ground = pygame.Rect(0, HEIGHT//2 + 150, WIDTH, HEIGHT - HEIGHT//2 + 150)

    def on_cleanup(self):
        pygame.quit()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_render(self):
        pygame.display.set_caption(f"Platformer - FPS: {round(self.clock.get_fps(), 1)}")
        self.player.show(self._surface)
        pygame.draw.rect(self._surface, (0,125,75), self.ground)

    def on_loop(self):
        self.player.update(self.ground)

    def on_execute(self):
        self.on_init()
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self._surface.fill((0,0,0))
            self.on_render()
            self.on_loop()
            self.clock.tick(60)
            pygame.display.flip()
        self.on_cleanup()

    