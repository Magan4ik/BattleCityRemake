import pygame.sprite

from settings import *


class Button(pygame.sprite.Sprite):
    def __init__(self, img, x, y, w, h):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pressed = False

    def is_on(self):
        x, y = pygame.mouse.get_pos()
        if self.rect.collidepoint(x, y):
            return True
        return False

    def is_press(self):
        btn = pygame.mouse.get_pressed()
        if self.is_on() and btn[0] and not self.pressed:
            self.pressed = True
            return True
        if not btn[0]:
            self.pressed = False
        return False

    def update(self):
        self.is_press()

    def draw(self):
        win.blit(self.image, self.rect)