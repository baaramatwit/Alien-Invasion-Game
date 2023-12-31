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
            self.ship.update()
            self._update_screen()

    # Watch for keyboard and mouse events (helper method) _
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # Move ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

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
