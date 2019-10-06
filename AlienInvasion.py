import sys
import pygame
from pygame.sprite import Group
from pygame.time import Clock

from settings import Settings
from ship import Ship
from alien import Alien


class AlienInvasion:
    def __init__(self):
        self.settings = Settings()
        # Initialize pygame, settings and create screen object.
        pygame.init()
        self.init_window()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.clock = Clock()

        # Make a group to store bullets in.
        self.bullets = Group()
        # Make a group to store aliens in.
        self.aliens = Group()
        # Make a ship.
        self.ship = Ship(self)
        self.delta_time = .0
        self.font = pygame.font.SysFont("arial", 16)
        self.init_aliens()
        self.frame_time = 0

    def init_window(self):
        pygame.display.set_caption("Alien Invasion")

    def init_aliens(self):
        alien_columns = 10
        alien_rows = 3
        column_width = (self.settings.screen_width - 100) / alien_columns
        row_height = 150
        offset_x = 100
        offset_y = 100
        for y in range(0, alien_rows):
            for x in range(0, alien_columns):
                row_x_offset = y * 5
                row_speed = (1+y) * 0.3
                if y % 2 == 0:
                    direction = -1
                    flip = False
                else:
                    direction = 1
                    flip = True
                direction = direction * row_speed
                self.aliens.add(Alien(self, offset_x + row_x_offset + (column_width * x), offset_y + (row_height * y), direction, flip))

    def run(self):
        # Start the main loop for the game.
        while True:
            self.frame_time = int(pygame.time.get_ticks() / 1000)
            self.check_events()
            self.ship.update()
            self.bullets.update()
            self.aliens.update()
            self.check_bullet_collisions()
            self.update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.delta_time = self.clock.tick(self.settings.frame_rate)/1000.0

    def check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                self.ship.check_events(event)

    def render_log(self):
        text = self.font.render(str(int(self.clock.get_fps())) + " time: " + str(self.frame_time) + " bullets: " + str(len(self.bullets)) + " delta time: " + str(self.delta_time) + str(self.ship), True, (195, 0, 0))
        self.screen.blit(text, (20, 10))

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        # Redraw all bullets behind ship and aliens.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Redraw all bullets behind ship and aliens.
        for alien in self.aliens.sprites():
            alien.draw()

        self.render_log()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def check_bullet_collisions(self):
        for bullet in self.bullets.sprites():
            alien = pygame.sprite.spritecollideany(bullet, self.aliens)
            if alien is not None:
                bullet.destroy()
                alien.destroy()


game = AlienInvasion()
game.run()
