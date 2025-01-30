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


class Entity(GameSprite):
    def __init__(self, image, x, y, width, height, speed, hp):
        super().__init__(image, x, y, width, height)
        self.speed = speed
        self.hp = hp


class Obstacle(GameSprite):
    def __init__(self, image, x, y, hp, immortal):
        super().__init__(image, x, y, WALL_SIZE, WALL_SIZE)
        self.immortal = immortal
        self.hp = hp


class Bullet(Entity):
    def __init__(self, image, x, y, width, height, speed, direction):
        super().__init__(image, x, y, width, height, speed, 1)
        self.direction = direction

    def update(self):
        #  direction - (nx, ny) | (0, 1), (1, 0), (-1, 0)
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]
        if (self.rect.x < 0 or self.rect.x > WIDTH) or (self.rect.y < 0 or self.rect.y >= HEIGHT):
            self.kill()
