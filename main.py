from settings import *
from sprites.player import Player
from sprites.enemy import Enemy, ToPlayerStrategy
from sprites.base_classes import Obstacle
from map_manager import MapManager


class GameController:
    def __init__(self):
        self.screen = "game"
        self.player = Player("textures/player_up1.png", 400, 500, 50, 50, 3, 100)
        self.map_manager = MapManager("maps/map1.txt")
        self.map_manager.load_map()

    def _game(self):
        win.fill((100, 200, 100))
        self.player.move()
        self.player.draw()
        walls.draw(win)
        for enemy in enemies:
            enemy.update(self.player)
            enemy.draw()
        bullets.update()
        bullets.draw(win)
        enemy_bullets.update()
        enemy_bullets.draw(win)
        collide = pygame.sprite.groupcollide(walls, bullets, True, True)
        collide = pygame.sprite.groupcollide(walls, enemy_bullets, True, True)
        collide = pygame.sprite.groupcollide(enemies, bullets, True, True)
        if pygame.sprite.spritecollide(self.player, enemies, False) or pygame.sprite.spritecollide(self.player, enemy_bullets, False):
            print("GAME OVER")
            self.screen = "menu"
        pygame.display.update()
        clock.tick(FPS)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def run(self):
        while True:
            self._handle_events()
            if self.screen == "game":
                self._game()


if __name__ == "__main__":
    game = GameController()
    game.run()
