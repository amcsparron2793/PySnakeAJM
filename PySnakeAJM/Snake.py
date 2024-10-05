from pygame import sprite, draw, Rect
from ConfigAndSettings import *


class Segment(sprite.Sprite):
    SEGMENT_LENGTH = 25
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
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        self.length = 1
        # Initialize snake_rect with initial position and size
        self.snake_rect = Rect(0, 0, Segment.SEGMENT_LENGTH, Segment.SEGMENT_WIDTH)
        self.center_snake()

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """ Update the snake's position based on the movement flag. """
        # FIXME: cant change direction until a wall is hit
        if self.moving_right and self.snake_rect.right < self.screen_rect.right:
            self.snake_rect.x += self.settings.snake_speed
        elif self.moving_right and self.snake_rect.right == self.screen_rect.right:
            self.moving_right = False

        if self.moving_left and self.snake_rect.left > 0:
            self.snake_rect.x -= self.settings.snake_speed
        elif self.moving_left and self.snake_rect.left == 0:
            self.moving_left = False

        if self.moving_up and self.snake_rect.top > 0:
            self.snake_rect.y -= self.settings.snake_speed
        elif self.moving_up and self.snake_rect.top == 0:
            self.moving_up = False

        if self.moving_down and self.snake_rect.bottom < self.screen_rect.bottom:
            self.snake_rect.y += self.settings.snake_speed
        elif self.moving_down and self.snake_rect.bottom == self.screen_rect.bottom:
            self.moving_down = False

        # if self.moving_up or self.moving_down or self.moving_left:
        #     print(
        #         f"Moving Right: {self.moving_right}, Moving Left: {self.moving_left}, Moving Up: {self.moving_up}, Moving Down: {self.moving_down}")
        #     print(f"Snake Position: x={self.snake_rect.x}, y={self.snake_rect.y}")

    def biltme(self):
        """ Draw the snake at its current location. """
        self.screen.fill(BLACK)  # Clear screen with black before drawing
        draw.rect(self.screen, WHITE, self.snake_rect)

    def center_snake(self):
        """ Center the snake on screen."""
        self.snake_rect.center = self.screen_rect.center
