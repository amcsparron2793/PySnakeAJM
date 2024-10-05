from pygame import sprite

import random

from ConfigAndSettings.Button import Button
from ConfigAndSettings.HIDEventHandler import _HIDEventHandler
from ConfigAndSettings.Settings import Settings

class InitPySnakeAJM(_HIDEventHandler):
    def __init__(self):
        self.settings = Settings()
        self.play_button = Button(self, "Start")
        self.running = False
        self.game_active = False
        self.segments = sprite.Group()
        self._get_random_apple_location()

    def _get_random_apple_location(self):
        self.apple_x = random.randint(0, self.settings.screen_width)
        self.apple_y = random.randint(0, self.settings.screen_height)