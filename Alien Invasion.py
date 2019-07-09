import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        self.settings = Settings()
        self.initWindow()
        # Initialize pygame, settings and create screen object.
        pygame.init()
        self.initWindow()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Make a group to store bullets in.
        self.bullets = Group()
        # Make a ship.
        self.ship = Ship(self)

    def initWindow(self):
        pygame.display.set_caption("Alien Invasion")

    def run(self):
        # Start the main loop for the game.
        while True:
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                self.ship.check_events(event)

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        # Redraw all bullets behind ship and aliens.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


game = AlienInvasion()
game.run()
