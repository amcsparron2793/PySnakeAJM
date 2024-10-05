import pygame


class _HIDEventHandler:
    def _check_keydown_events(self, event):
        """
        This method is responsible for handling keydown events in the game.

        Args:
            event (pygame.event.Event): The keydown event captured by the game.

        Returns:
            None

        Raises:
            None

        Example:
            _check_keydown_events(event)
        """
        if event.key == pygame.K_RIGHT:
            # move the snake to the right
            self.snake.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the snake to the left
            self.snake.moving_left = True
        elif event.key == pygame.K_UP:
            self.snake.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.snake.moving_down = True

        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            # self.sb.write_highscore()
            # if q or esc is pressed pause the game
            self.game_active = False
            if event.key == pygame.K_q and not self.game_active:
                self.running = False
                self.show_leaderboard = False

        elif event.key == pygame.K_F12:
            self.settings.toggle_fullscreen()
        elif event.key == pygame.K_m:
            #self.sounds.toggle_mute()
            # TODO: sound
            ...

    def _check_keyup_events(self, event):
        """
        This method is responsible for handling key-up events in the game.

        :param event: The key-up event that is triggered
        :type event: pygame.event.Event
        """
        # if event.key == pygame.K_RIGHT:
        #     self.snake.moving_right = False
        # elif event.key == pygame.K_LEFT:
        #     self.snake.moving_left = False
        # elif event.key == pygame.K_UP:
        #     self.snake.moving_up = False
        # elif event.key == pygame.K_DOWN:
        #     self.snake.moving_down = False

    def _check_play_button(self, mouse_pos):
        """

        Check if the play button is clicked.

        Parameters:
        - `mouse_pos` : tuple
            The x and y coordinates of the mouse position.

        Returns:
        - None

        Behavior:
        - Checks if the play button is clicked by comparing the mouse position with the rectangle of the play button.
        - If the play button is clicked and the game is not active, it resets the game settings and statistics and sets `game_active` to True.

        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # reset the game settings
            # reset the game statistics
            self.game_active = True