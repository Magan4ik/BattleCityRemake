import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

WALL_SIZE = 50

walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
