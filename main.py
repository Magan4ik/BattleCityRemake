from settings import *
from sprites.player import Player
from sprites.enemy import Enemy, ToPlayerStrategy
from sprites.base_classes import Obstacle
from map_manager import MapManager
from ui import Button


class GameController:
    def __init__(self):
        self.screen = "menu"
        self.player = Player("textures/player_up1.png", 400, 500, 50, 50, 3, 100)
        self.map_manager = MapManager("maps/map1.txt")
        self.map_manager.load_map()
        self.button_start = Button("textures/button_start.png", WIDTH // 3, HEIGHT // 2, 200, 100)

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
        if pygame.sprite.spritecollide(self.player, enemies, False) or pygame.sprite.spritecollide(self.player,
                                                                                                   enemy_bullets,
                                                                                                   False):
            print("GAME OVER")
            self.screen = "menu"

    def _menu(self):
        win.fill((100, 200, 100))
        self.button_start.draw()
        if self.button_start.is_press():
            self.player = Player("textures/player_up1.png", 400, 500, 50, 50, 3, 100)
            self.map_manager.load_map()
            bullets.empty()
            enemy_bullets.empty()
            self.screen = "game"

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def run(self):
        while True:
            self._handle_events()
            if self.screen == "menu":
                self._menu()
            if self.screen == "game":
                self._game()
            pygame.display.update()
            clock.tick(FPS)


if __name__ == "__main__":
    game = GameController()
    game.run()
