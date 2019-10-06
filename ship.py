import pygame
from bullet import Bullet


class Ship:

    def __init__(self, game):
        """Initialize the ship and set its starting position."""
        self.game = game

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = game.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        # velocity of the ship
        self.velocity = .0

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        # speed, pixels per second
        self.speed = self.game.settings.ship_speed_factor * 100
        self.breakSpeed = self.game.settings.ship_speed_factor * 100
        self.width = self.rect.right - self.rect.left
        self.max_offset_left = self.width / 2.0
        self.max_offset_right = self.screen_rect.right - (self.width / 2.0)

    def shoot(self):
        # Create a new bullet and add it to the bullets group.
        Bullet(self.game)

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

    def slow_down(self):
        if self.velocity < 0:
            self.velocity += min(abs(self.velocity), self.game.delta_time * self.breakSpeed)

        elif self.velocity > 0:
            self.velocity -= min(abs(self.velocity), self.game.delta_time * self.breakSpeed)
    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.velocity += self.game.delta_time * self.speed
        elif self.moving_left:
            self.velocity -= self.game.delta_time * self.speed
        else:
            self.slow_down()

        self.center += self.game.delta_time * self.velocity

        if self.center < self.max_offset_left:
            self.center = self.max_offset_left
            self.velocity = 0
        if self.center > self.max_offset_right:
            self.center = self.max_offset_right
            self.velocity = 0

        self.rect.centerx = self.center


    def draw(self):
        """Draw the ship at its current location"""
        self.game.screen.blit(self.image, self.rect)

    def __str__(self):
        return "ship: x: " + str(self.rect.centerx)\
               + ", move left: " + str(self.moving_left) \
               + ", move right: " + str(self.moving_right) \
               + ", movement speed: " + str(self.speed) \
               + ", delta speed:" + str(self.game.delta_time * self.game.settings.ship_speed_factor)\
               + ", velocity:" + str(self.velocity)
