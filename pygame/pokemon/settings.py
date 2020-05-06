import os
import math

# game window
WIDTH, HEIGHT = 640, 480
CANVAS_WIDTH, CANVAS_HEIGHT = 640, 480

# game settings
TILE_SIZE = 32
TILE_SHAPE = (TILE_SIZE, TILE_SIZE)
POWER = int(math.log2(TILE_SIZE))
T_WIDTH = CANVAS_WIDTH // TILE_SIZE
T_HEIGHT = CANVAS_HEIGHT // TILE_SIZE

# player
PLAYER_POSITION = [T_WIDTH // 2, T_HEIGHT // 2]

# paths
RESOURCE_PATH = os.path.join("game", "resources")
SPRITE_CHARACTER_PATH = os.path.join(RESOURCE_PATH, "img", "character")
SPRITE_MAP_PATH = os.path.join(RESOURCE_PATH, "img", "maps")

# infinity
INF = float('inf')

# constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# colors
DEFAULT_COLOR = (75,0,125)