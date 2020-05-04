import os
import math

# game window
WIDTH, HEIGHT = 640, 480
CANVAS_WIDTH, CANVAS_HEIGHT = 640, 480

# map settings
TILE_SIZE = 32
POWER = int(math.log2(TILE_SIZE))
T_WIDTH = CANVAS_WIDTH // TILE_SIZE
T_HEIGHT = CANVAS_HEIGHT // TILE_SIZE

# paths
RESOURCE_PATH = os.path.join("game", "resources")

# infinity
INF = float('inf')

# constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3