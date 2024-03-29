import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.game = game
        self.game.bullets.add(self)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.game.settings.bullet_width, self.game.settings.bullet_height)
        self.rect.top = game.ship.rect.top
        self.rect.centerx = game.ship.rect.centerx

        # Store the bullet's position as a decimal value.

        self.y = float(self.rect.y)

        self.color = game.settings.bullet_color
        self.speed_factor = game.settings.bullet_speed_factor * 100

    def update(self):
        """Move the bullet up the screen."""

        # bullet is out of screen. can be destroyed
        if self.rect.bottom < 0:
            self.destroy()
        # Update the decimal postion of the bullet.
        self.y -= self.game.delta_time * self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.game.screen, self.color, self.rect)

    def destroy(self):
        self.game.bullets.remove(self)
