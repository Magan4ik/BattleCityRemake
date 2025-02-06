from settings import *
from .base_classes import Entity, Bullet
import math


class Enemy(Entity):
    def __init__(self, image, x, y, width, height, speed, hp, move_strategy):
        super().__init__(image, x, y, width, height, speed, hp)
        self.rate = 70
        self.reload = 0
        self.move_strategy = move_strategy
        self.direction = (0, -1)

    def fire(self):
        bullet = Bullet("textures/bullet.jpg", self.rect.centerx, self.rect.centery, 10, 15, 10, self.direction)
        enemy_bullets.add(bullet)

    def update(self, *args, **kwargs):
        self.move_strategy.move(self, *args, **kwargs)
        if self.reload >= self.rate:
            self.fire()
            self.reload = 0
        self.reload += 1

    def collide_walls(self, x, y):
        for wall in walls:
            if wall.rect.colliderect(pygame.Rect(x, y, self.rect.width, self.rect.height)):
                return True
        return False


class ToPlayerStrategy:
    def move(self, entity, player):
        dx = player.rect.x - entity.rect.x
        dy = player.rect.y - entity.rect.y

        new_x = entity.rect.x
        new_y = entity.rect.y

        if abs(dx) > abs(dy):
            temp_x = entity.rect.x + entity.speed * (1 if dx > 0 else -1)
            if not entity.collide_walls(temp_x, entity.rect.y):
                new_x = temp_x
            elif not entity.collide_walls(entity.rect.x, entity.rect.y + entity.speed * (1 if dy > 0 else -1)):
                new_y = entity.rect.y + entity.speed * (1 if dy > 0 else -1)
        else:
            temp_y = entity.rect.y + entity.speed * (1 if dy > 0 else -1)
            if not entity.collide_walls(entity.rect.x, temp_y):
                new_y = temp_y
            elif not entity.collide_walls(entity.rect.x + entity.speed * (1 if dx > 0 else -1), entity.rect.y):
                new_x = entity.rect.x + entity.speed * (1 if dx > 0 else -1)

        if new_x > entity.rect.x:
            entity.rotate(270)
            entity.direction = (1, 0)
        elif new_x < entity.rect.x:
            entity.rotate(90)
            entity.direction = (-1, 0)

        if new_y > entity.rect.y:
            entity.rotate(180)
            entity.direction = (0, 1)
        elif new_y < entity.rect.y:
            entity.direction = (0, -1)

        entity.rect.x = new_x
        entity.rect.y = new_y
