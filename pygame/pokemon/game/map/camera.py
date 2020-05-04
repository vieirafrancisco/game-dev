import math

from settings import *

class Camera:
    def __init__(self, player, tmap):
        self.player = player
        self.tmap = tmap
        self.dx, self.dy = 0, 0

    def show(self, master_surface):
        # corner pins
        x0 = self.dx >> POWER
        x1 = (self.dx >> POWER) + T_WIDTH
        y0 = self.dy >> POWER
        y1 = (self.dy >> POWER) + T_HEIGHT
        print(x0, x1, y0, y1)
        for j in range(y0, y1 + 1):
            y = (j * TILE_SIZE - self.dy)
            for i in range(x0, x1 + 1):
                x = (i * TILE_SIZE - self.dx)
                dest = (x, y)
                if i >= 0 and j >= 0 and i < self.tmap.cols and j < self.tmap.rows:
                    entity = self.tmap.get_entity(i, j)
                    entity.start(self, self.tmap.surface, dest)
                else:
                    self.tmap.surface.blit(self.tmap.src_img, dest, self.tmap.tiles["default"])
        master_surface.blit(self.tmap.surface, (0,0))
        self.player.show(master_surface)

    def update(self):
        self.player.move(self)

    def is_player(self, x, y):
        if (x, y) == self.player.get_pos():
            return True
        else:
            return False