import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y, w, h, speed=5):
        self.rect = pygame.Rect(x, y, w, h)
        self.speed = speed
        m_x, m_y = pygame.mouse.get_pos()
        self.mouse_rect = pygame.Rect(m_x-5, m_y-5, 10, 10)
        self.mouse_color = (255,255,255)

    def show(self, surface):
        pygame.draw.rect(surface, (255,255,255), self.rect)
        pygame.draw.rect(surface, self.mouse_color, self.mouse_rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_s]:
            self.rect.y += self.speed
        if keys[K_a]:
            self.rect.x -= self.speed
        m_x, m_y = pygame.mouse.get_pos()
        self.mouse_rect = pygame.Rect(m_x-5, m_y-5, 10, 10)
        if pygame.mouse.get_pressed()[0]:
            self.mouse_color = (255,0,0)
        else:
            self.mouse_color = (255,255,255)
        
        
