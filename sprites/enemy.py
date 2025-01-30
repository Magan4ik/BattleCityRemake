from settings import *
from .base_classes import Entity


class Enemy(Entity):
    def __init__(self, image, x, y, width, height, speed, hp, move_strategy):
        super().__init__(image, x, y, width, height, speed, hp)
        self.rate = 20
        self.move_strategy = move_strategy

    def fire(self):
        pass

    def update(self):
        self.move_strategy.move(self)


class ToPlayerStrategy:
    def move(self, entity):
        pass
