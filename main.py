from settings import *
from sprites.base_classes import GameSprite


class GameController:
    def __init__(self):
        self.screen = "game"

    def _game(self):
        win.fill((100, 200, 100))
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
