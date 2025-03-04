import pygame
from ..engine.BaseObject import BaseObject

class MovableObject(BaseObject):
    def __init__(self, x, y, width, height, color, speed=5):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
