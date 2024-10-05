"""
PySnakeAJM.py

Snake for Python

"""
import pygame
from ConfigAndSettings.Button import Button
from ConfigAndSettings.HIDEventHandler import _HIDEventHandler
from ConfigAndSettings.Settings import Settings
from Snake import Segment, Snake



class PySnakeAJM(_HIDEventHandler):
    clock = pygame.time.Clock()
    def __init__(self):
        pygame.init()
        self.running = False
        self.game_active = False
        self.settings = Settings()

        self.play_button = Button(self, "Start")
        self.segments = pygame.sprite.Group()
        self.snake = Snake(self)

    def _check_system_events(self):
        """
        Checks for system events and performs corresponding actions.

        This method checks for system events using the `pygame.event.get()` function. It iterates over each event and performs actions based on the event type. The following event types are checked:

        - `pygame.QUIT`: If the event type is `pygame.QUIT`, the `pygame.quit()` function is called to quit the game.
        - `pygame.MOUSEBUTTONDOWN`: If the event type is `pygame.MOUSEBUTTONDOWN`, the current mouse position is obtained using `pygame.mouse.get_pos()` and passed to the `_check_play_button()` method.
        - `pygame.KEYDOWN`: If the event type is `pygame.KEYDOWN`, the event is passed to the `_check_keydown_events()` method.
        - `pygame.KEYUP`: If the event type is `pygame.KEYUP`, the event is passed to the `_check_keyup_events()` method.

        This method should be called in the game loop to continuously check for system events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def GameLoop(self):
        while self.running:
            self._check_system_events()
            self.snake.update()
            self.snake.biltme()

            pygame.display.flip()
            self.clock.tick(self.settings.fps)


if __name__ == '__main__':
    game = PySnakeAJM()
    game.running = True
    game.GameLoop()
