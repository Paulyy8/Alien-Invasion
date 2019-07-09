import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.game = game

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.game.settings.bullet_width, self.game.settings.bullet_height)
        self.rect.top = game.ship.rect.top
        self.rect.centerx = game.ship.rect.centerx

        # Store the bullet's postion as a decimal value.

        self.y = float(self.rect.y)

        self.color = game.settings.bullet_color
        self.speed_factor = game.settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal postion of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.game.screen, self.color, self.rect)

        
