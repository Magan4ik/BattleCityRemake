from settings import *


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(image), (width, height))
        self.start_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self):
        win.blit(self.image, self.rect)
