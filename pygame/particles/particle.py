import pygame

class Particle:
    def __init__(self, x, y, radius=3):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = [0,0]
        
    def draw(self, surface):
        pygame.draw.circle(surface, (255,255,255), (int(self.x), int(self.y)), self.radius)

    def move(self, dest):
        acc = (dest[0] - self.x) * 0.1, (dest[1] - self.y) * 0.1
        self.vel[0] += acc[0]
        self.vel[1] += acc[1]
        self.x += self.vel[0]
        self.y += self.vel[1]

        
        


