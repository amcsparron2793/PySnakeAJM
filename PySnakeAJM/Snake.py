from pygame import sprite, draw, Rect, Surface
from pygame.transform import rotate
from ConfigAndSettings import *


class Segment(sprite.Sprite):
    SEGMENT_LENGTH = 25
    SEGMENT_WIDTH = 10

    def __init__(self, ps_game):
        self.game = ps_game
        self.settings = self.game.settings
        super().__init__()
        self.first_seg_rect = Rect(0, 0, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH)

    def draw(self, x, y):
        rect = Rect(x, y, self.SEGMENT_LENGTH, self.SEGMENT_WIDTH)
        draw.rect(self.settings.screen, WHITE, rect)


class Snake(Segment):
    def __init__(self, ps_game):
        self.game = ps_game
        super().__init__(self.game)

        self.settings = self.game.settings
        self.screen = self.settings.screen
        self.screen_rect = self.screen.get_rect()
        self.length = 1
        self.snake_color = GREEN
        self.original_snake_image = Surface((self.SEGMENT_LENGTH, self.SEGMENT_WIDTH))
        self.original_snake_image.fill(self.snake_color)
        self.snake_img = self.original_snake_image


        # Initialize rect with initial position and size
        self.rect = self.snake_img.get_rect()
        self.first_seg_rect = self.rect
        self.center_snake()
        self.segments = [self.first_seg_rect]

        self.direction = ''  # Initial direction


    @property
    def first_segment_location(self):
        return self.first_seg_rect.x, self.first_seg_rect.y

    @property
    def front_of_snake(self):
        return self.first_seg_rect.midleft


    def update(self):
        # FIXME: THIS DOESNT WORK?
        # Assign default value to new_head using the current position
        new_head = self.first_seg_rect.copy()
        # Move all segments
        if self.direction == 'RIGHT' and self.first_seg_rect.right < self.screen_rect.right:
            new_head = self.first_seg_rect.move(self.settings.snake_speed, 0)
        elif self.direction == 'LEFT' and self.first_seg_rect.left > 0:
            new_head = self.first_seg_rect.move(-self.settings.snake_speed, 0)
        elif self.direction == 'UP' and self.first_seg_rect.top > 0:
            new_head = self.first_seg_rect.move(0, -self.settings.snake_speed)
        elif self.direction == 'DOWN' and self.first_seg_rect.bottom < self.screen_rect.bottom:
            new_head = self.first_seg_rect.move(0, self.settings.snake_speed)

        # Insert new head segment and remove the last segment if the snake has not grown
        self.segments.insert(0, new_head)
        if len(self.segments) > self.length:
            self.segments.pop()

    def blitme(self):
        """ Draw the snake at its current location. """
        for segment in self.segments:
            draw.rect(self.settings.screen, self.snake_color, segment)

    def grow(self):
        self.length += 1

    def rotate_image(self):
        if self.direction == 'RIGHT':
            self.original_snake_image = rotate(self.original_snake_image, 0)
        elif self.direction == 'LEFT':
            self.original_snake_image = rotate(self.original_snake_image, 180)
        elif self.direction == 'UP':
            self.original_snake_image = rotate(self.original_snake_image, 90)
        elif self.direction == 'DOWN':
            self.original_snake_image = rotate(self.original_snake_image, -90)

    def center_snake(self):
        """ Center the snake on screen."""
        self.rect.center = self.screen_rect.center
