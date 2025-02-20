from settings import *
from sprites.base_classes import Obstacle
from sprites.enemy import Enemy, ToPlayerStrategy


class MapManager:
    def __init__(self, filename):
        self.filename = filename

    def load_map(self):
        walls.empty()
        enemies.empty()
        with open(self.filename, 'r', encoding='utf-8') as map:
            for y, line in enumerate(map):
                for x, sym in enumerate(line):
                    if sym == "W":
                        walls.add(Obstacle("textures/wall.png", x*WALL_SIZE, y*WALL_SIZE, 5, False))
                    elif sym == "E":
                        enemies.add(Enemy("textures/enemy.png", x*WALL_SIZE, y*WALL_SIZE, 50, 50, 2, 2, ToPlayerStrategy()))
                    elif sym == "-":
                        pass

