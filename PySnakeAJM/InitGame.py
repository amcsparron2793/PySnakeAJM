from pygame import sprite
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