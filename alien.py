import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class of an Alien enemy """

    def __init__(self, game, centerx, centery, direction, flip):
        super().__init__()
        self.game = game
        self.game.aliens.add(self)
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.center = self.rect.centerx
        self.speed = self.game.settings.alien_speed_factor * 100
        self.direction = direction
        self.last_frame = 0
        self.flip = flip

    def update(self):
        if self.game.frame_time != self.last_frame:
            self.last_frame = self.game.frame_time
            self.direction *= -1
        self.center += self.direction * (self.speed * self.game.delta_time)
        self.rect.centerx = self.center

    def draw(self):
        """Draw the alien at its current location"""
        if self.flip:
            self.game.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
        else:
            self.game.screen.blit(self.image, self.rect)


    def destroy(self):
        self.game.aliens.remove(self)

