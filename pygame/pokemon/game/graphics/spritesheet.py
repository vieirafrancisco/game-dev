import pygame
import json
import os

from settings import *
from game.graphics.tile import Tile

def get_tiles(path, file_name):
    tiles = {}
    with open(os.path.join(RESOURCE_PATH, "json", path, f"{file_name}.json"), "r") as f:
        content = json.load(f)
        for tile, attr in content[file_name].items():
            tiles[tile] = Tile(*list(attr.values()))
    return tiles

def load_image(path):
    image = pygame.image.load(os.path.join(RESOURCE_PATH, "spritesheets", path))
    return image.convert()

def get_surface(shape):
    image = pygame.Surface(shape).convert()
    color = PINK_BACKGROUD_COLORKEY
    image.fill(color)
    image.set_colorkey(color)
    return image

class Spritesheet:
    def __init__(self, path, file_name):
        self.image = load_image(os.path.join(path, f"{file_name}.png"))
        self.tiles = get_tiles(path, file_name)

    def get_tile_image(self, name):
        tile = self.tiles[name]
        image = get_surface(tile.shape)
        image.blit(self.image, (0, 0), tile.rect)
        return image

    def get_tile_image_by_position(self, x, y, w, h):
        image = get_surface((w, h))
        image.blit(self.image, (0, 0), (x, y, w, h))
        return image