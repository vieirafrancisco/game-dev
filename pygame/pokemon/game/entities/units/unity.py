from abc import abstractmethod

from game.entities.entity import Entity
from settings import *

class Unity(Entity):
    def __init__(self, posx, posy, health, speed, solid=False):
        Entity.__init__(self, posx, posy, solid)
        self.health = health
        self.speed = speed

    @abstractmethod
    def move(self, camera):
        pass