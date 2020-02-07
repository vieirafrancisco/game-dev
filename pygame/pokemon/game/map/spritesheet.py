import pygame
import json
import os

from settings import *

class SpriteSheet:
    def __init__(self, file_name):
        self.image = pygame.image.load(os.path.join(RESOURCE_PATH, "spritesheets", file_name))
        with open(os.path.join(RESOURCE_PATH, "json", "spritesheets.json"), "r") as f:
            self.json = json.load(f)
        self.tiles = {}
        for tile in self.json[file_name]:
            pos = self.json[file_name][tile]
            self.tiles[tile] = pygame.Rect((pos[0] * TILE_SIZE, pos[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))