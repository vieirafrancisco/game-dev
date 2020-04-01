import os

# game window
WIDTH, HEIGHT = 640, 480

# map settings
TILE_SIZE = 32
T_WIDTH = WIDTH // TILE_SIZE
T_HEIGHT = HEIGHT // TILE_SIZE

# paths
RESOURCE_PATH = os.path.join("game", "resources")

# infinity
INF = float('inf')

# constants
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3