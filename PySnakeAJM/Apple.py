from pygame import sprite, draw, Rect
from ConfigAndSettings import *

class Apple(sprite.Sprite):
    SEGMENT_LENGTH = 10
    SEGMENT_WIDTH = 10

    def __init__(self, ps_game, x: int, y: int):
        super().__init__()
        self.game = ps_game
        self.settings = self.game.settings
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH)

    def blitme(self):
        """ Draw the Apple at its current location. """
        draw.rect(self.screen, RED, self.rect)
