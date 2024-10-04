from pygame import sprite, draw, Rect
from ConfigAndSettings import *


class Segment(sprite.Sprite):
    SEGMENT_LENGTH = 50
    SEGMENT_WIDTH = 10

    def __init__(self, ps_game, x: int, y: int):
        self.x = x
        self.y = y
        self.game = ps_game
        self.settings = self.game.settings
        super().__init__()

    def draw(self, x, y):
        rect = Rect(x, y, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH)
        draw.rect(self.settings.screen, WHITE, rect)


class Snake(sprite.Sprite):
    def __init__(self, ps_game):
        super().__init__()
        self.game = ps_game
        self.settings = self.game.settings
        self.screen = self.game.screen
        self.length = 0
        self.screen_rect = self.screen.get_rect()
        # TODO: add snake rect
        # TODO: add snake movement

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the ships position based on the movement flag. """
        # updates the ships x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.snake_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.snake_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def biltme(self):
        """ Draw the ship at its current location. """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ Center the ship on screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def move_left(self):
        if self.x > 0:
            self.x -= self.settings.ship_speed

    def move_right(self):
        if self.x < self.settings.screen_width - self.width:
            self.x += self.settings.ship_speed

