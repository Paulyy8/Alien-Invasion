import pygame
from bullet import Bullet


class Ship:

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.game = game

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def shoot(self):
        # Create a new bullet and add it to the bullets group.
        self.game.bullets.add(Bullet(self.game))

    def check_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.on_keydown(event)
        elif event.type == pygame.KEYUP:
            self.on_keyup(event)

    def on_keydown(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            self.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.shoot()

    def on_keyup(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.rect.centerx += self.game.settings.ship_speed_factor
        elif self.moving_left:
            self.rect.centerx -= self.game.settings.ship_speed_factor
        
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right

    def draw(self):
        """Draw the ship at its current location"""
        self.game.screen.blit(self.image, self.rect)
