import pygame
from pygame.locals import *

from settings import *
from game.sprites.player import Player
from game.sprites.wall import Wall

class Game:
    def __init__(self):
        self._surface = None
        self._running = False
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._running = True
        self._surface = pygame.display.set_mode(SIZE)
        self.sprites = pygame.sprite.Group()
        self.player = Player(self, 64, 64)
        
    def on_cleanup(self):
        pygame.quit()

    def on_render(self):
        for i in range(TILE_SIZE, WIDTH, TILE_SIZE):
            pygame.draw.line(self._surface, GRAY, (i, 0), (i, HEIGHT))
        for j in range(TILE_SIZE, HEIGHT, TILE_SIZE):
            pygame.draw.line(self._surface, GRAY, (0, j), (WIDTH, j))
        self.sprites.draw(self._surface)
        for i in range(128, 3 * 128, 32):
            self.sprites.add(Wall(self, i, 128))

    def on_loop(self):
        pygame.display.set_caption(f"Robot - FPS: {round(self.clock.get_fps(), 1)}")
        self.sprites.update()
        
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        if event.type == KEYDOWN:
            if event.key == K_UP or event.key == K_w:
                self.player.rect.y -= TILE_SIZE
            if event.key == K_RIGHT or event.key == K_d:
                self.player.rect.x += TILE_SIZE
            if event.key == K_DOWN or event.key == K_s:
                self.player.rect.y += TILE_SIZE
            if event.key == K_LEFT or event.key == K_a:
                self.player.rect.x -= TILE_SIZE

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