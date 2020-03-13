import os
import pygame

from player import Player
from particle import Particle

class Game:
    def __init__(self):
        self.size = 400, 400
        self.running = False
        self._disp_window = None
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self.running = True
        self._disp_window = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Particles")
        self.player = Player(200,380)
        self.p = Particle(200,380)

    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        self.player.draw(self._disp_window)
        print(pygame.mouse.get_pressed()[0])
        if pygame.mouse.get_pressed()[0]:
            x, y = pygame.mouse.get_pos()
            pygame.draw.rect(self._disp_window, (0,125,0), (x - 4, y - 4, 8, 8))
        self.p.draw(self._disp_window)

    def on_loop(self):
        self.p.move((400, 0))

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