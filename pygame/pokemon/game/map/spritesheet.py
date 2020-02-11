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
        for tile, attr  in self.json[file_name].items():
            self.tiles[tile] = Tile(attr["pos"], tuple(attr["rgba"]), attr["solid"])

    def get_objects(self):
        return self.image, self.tiles