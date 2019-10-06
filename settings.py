class Settings:
    """A class to store all settings for Alien invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # game settings
        # frame rate 0 it will have no frame rate delay
        self.frame_rate = 0

        # Ship settings
        self.ship_speed_factor = 16
        self.ship_break_factor = 40

        # Bullet settings
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60

        # Alien settings
        self.alien_speed_factor = 1
