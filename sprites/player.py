from .base_classes import Entity
from settings import *


class Player(Entity):
    def __init__(self, image, x, y, width, height, speed, hp):
        super().__init__(image, x, y, width, height, speed, hp)
        self.rate = 95

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def fire(self):
        pass
