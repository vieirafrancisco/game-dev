import os
import pygame
from pygame.locals import *

from settings import *
from game.map.map import Map
from game.entities.units.player import Player
from game.entities.units.enemy import Enemy

class Game:
    def __init__(self):
        self.size = WIDTH, HEIGHT
        self.running = False
        self.surface = None
        self.clock = pygame.time.Clock()

    def init(self):
        pygame.init()
        self.running = True
        self.surface = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokémon")
        self.sprites = pygame.sprite.Group()
        self.map = Map(os.path.join("game","resources", "img", "maps", "map06.png"))
        self.player = Player(self, *PLAYER_POSITION, 100, 2)
        self.sprites.add(self.map)
        self.sprites.add(self.player)
        self.enemy = Enemy(10, 9, False, 100, 50, walk_range=3)
        self.enemy2 = Enemy(2, 8, False, 100, 50, walk_range=3)
        self.enemy3 = Enemy(13, 3, False, 100, 50, walk_range=3)
        self.map.add_entity(self.enemy)
        self.map.add_entity(self.enemy2)
        self.map.add_entity(self.enemy3)

    def cleanup(self):
        pygame.quit()

    def render(self):
        self.sprites.draw(self.surface)

    def loop(self):
        self.sprites.update()
        pygame.display.set_caption(f"Pokémon - FPS: {round(self.clock.get_fps(), 1)}")

    def event(self, event):
        if event.type == QUIT:
            self.running = False

    def execute(self):
        self.init()
        while(self.running):
            for event in pygame.event.get():
                self.event(event)
            self.surface.fill((0,0,0))
            self.loop()
            self.render()
            pygame.display.flip()
            self.clock.tick(60)
        self.cleanup()