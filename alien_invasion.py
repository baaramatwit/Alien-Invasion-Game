# empty pygame window , creating class to represent the game
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    # Class to manage game assets and behavior
    def __init__(self):
        # Initialize game and create game resources
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        # Starting main loop for the game
        while True:
            self._check_events()
            self._update_screen()

    # Watch for keyboard and mouse events (helper method) _
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    # Move ship to the right
                    self.ship.rect.x += 1

    def _update_screen(self):
        # redraw screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Make screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game and run the game
    ai = AlienInvasion()
    ai.run_game()
