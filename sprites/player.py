import pygame

from .base_classes import Entity, Bullet
from settings import *


class Player(Entity):
    def __init__(self, image, x, y, width, height, speed, hp):
        super().__init__(image, x, y, width, height, speed, hp)
        self.rate = 50
        self.reload = 0
        self.direction = (0, -1)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not (self._collide_walls(self.rect.x, self.rect.y - self.speed)):
            self.rect.y -= self.speed
            self.rotate(0)
            self.direction = (0, -1)
        if keys[pygame.K_s] and not (self._collide_walls(self.rect.x, self.rect.y + self.speed)):
            self.rect.y += self.speed
            self.rotate(180)
            self.direction = (0, 1)
        if keys[pygame.K_a] and not (self._collide_walls(self.rect.x - self.speed, self.rect.y)):
            self.rect.x -= self.speed
            self.rotate(90)
            self.direction = (-1, 0)
        if keys[pygame.K_d] and not (self._collide_walls(self.rect.x + self.speed, self.rect.y)):
            self.rect.x += self.speed
            self.rotate(270)
            self.direction = (1, 0)
        if keys[pygame.K_SPACE] and self.reload >= self.rate:
            self.fire()
            self.reload = 0
        self.reload += 1

    def _collide_walls(self, x, y):
        for wall in walls:
            if wall.rect.colliderect(pygame.Rect(x, y, self.rect.width, self.rect.height)):
                return True
        return False

    def fire(self):
        bullet = Bullet("textures/bullet.jpg", self.rect.centerx, self.rect.centery, 10, 15, 10, self.direction)
        bullets.add(bullet)
