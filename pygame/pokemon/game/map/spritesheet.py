import pygame
import json
import os

from settings import *
from game.map.tile import Tile

class SpriteSheet:
    def __init__(self, file_name):
        self.image = pygame.image.load(os.path.join(RESOURCE_PATH, "spritesheets", file_name))
        with open(os.path.join(RESOURCE_PATH, "json", "spritesheets.json"), "r") as f:
            self.json = json.load(f)
        self.tiles = {}
        for tile in self.json[file_name]:
            tile_info = self.json[file_name][tile]
            self.tiles[tile] = Tile(*tile_info["pos"], tile_info["solid"])

    def get_objects(self):
        return self.image, self.tiles