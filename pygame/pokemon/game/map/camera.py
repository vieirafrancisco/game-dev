import math

from settings import *

class Camera:
    def __init__(self, master):
        self.master = master
        self.dx, self.dy = 0, 0

    def show(self, tmap):
        # corner pins
        x0 = self.dx >> POWER
        x1 = (self.dx >> POWER) + T_WIDTH
        y0 = self.dy >> POWER
        y1 = (self.dy >> POWER) + T_HEIGHT
        #print(x0, x1, y0, y1)
        for j in range(y0, y1 + 1):
            y = (j * TILE_SIZE - self.dy)
            for i in range(x0, x1 + 1):
                x = (i * TILE_SIZE - self.dx)
                dest = (x, y)
                if i >= 0 and j >= 0 and i < tmap.cols and j < tmap.rows:
                    entity = tmap.get_entity(i, j)
                    entity.start(tmap, tmap.image, dest)
                else:
                    tmap.image.blit(tmap.src, dest, tmap.tiles["default"])
        self.master.blit(tmap.image, (0,0))