from game.entities.entity import Entity
from settings import *

class Ground(Entity):
    def __init__(self, posx, posy, solid=False):
        Entity.__init__(self, posx, posy, solid)
        
