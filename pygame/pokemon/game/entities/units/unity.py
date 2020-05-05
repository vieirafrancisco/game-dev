from game.entities.entity import Entity
from settings import *

class Unity(Entity):
    def __init__(self, x, y, solid, health, speed):
        Entity.__init__(self, x, y, solid)
        self.health = health
        self.speed = speed