import pygame

from .base_classes import Entity
from settings import *


class Player(Entity):
    def __init__(self, image, x, y, width, height, speed, hp):
        super().__init__(image, x, y, width, height, speed, hp)
        self.rate = 95

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not (self._collide_walls(self.rect.x, self.rect.y - self.speed)):
            self.rect.y -= self.speed
        if keys[pygame.K_s] and not (self._collide_walls(self.rect.x, self.rect.y + self.speed)):
            self.rect.y += self.speed
        if keys[pygame.K_a] and not (self._collide_walls(self.rect.x - self.speed, self.rect.y)):
            self.rect.x -= self.speed
        if keys[pygame.K_d] and not (self._collide_walls(self.rect.x + self.speed, self.rect.y)):
            self.rect.x += self.speed

    def _collide_walls(self, x, y):
        for wall in walls:
            if wall.rect.colliderect(pygame.Rect(x, y, self.rect.width, self.rect.height)):
                return True
        return False

    def fire(self):
        pass
