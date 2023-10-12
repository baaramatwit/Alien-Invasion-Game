# empty pygame window , creating class to represent the game

import sys

import pygame


class AlienInvasion:
    # Class to mnage game assets and behavior
    def __init__(self):
        # Initialize game and create game resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        # Starting main loop for the game
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Make screen visible
                pygame.display.flip()


if __name__ == '__main__':
    # Make an instance of the game and run the game
    ai = AlienInvasion()
    ai.run_game()
