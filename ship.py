# Class will manage behavior of the ship
import pygame


class Ship:

    def __init__(self, ai_game):
        # Initialize the ship and set the starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading the ship and getting its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False

    def update(self):
        # Update ship position based on the movement flag
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
