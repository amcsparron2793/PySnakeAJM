from pygame import display
from .utils import ColorConverter
from .PsConfig import PsConfig


class Settings:
    def __init__(self, **kwargs):
        self.config = PsConfig('config.ini', '../../cfg')
        self.config.GetConfig()

        self._setup_screen(kwargs.get('use_fullscreen',
                                      not self.config.getboolean('DEFAULT', 'windowed_mode')))

        self.leaderboard_db_location = self.config.get('LEADERBOARD', 'database_file_path')

    def _setup_screen(self, use_fullscreen):
        self.show_fps = self.config.getboolean('DEFAULT', 'show_fps')
        self.bg_color = ColorConverter.hex_to_rgb(self.config.get('DEFAULT', 'bg_color'))
        self.use_fullscreen = use_fullscreen
        self.screen_width = self.config.getint('DEFAULT', 'screen_width')
        self.screen_height = self.config.getint('DEFAULT', 'screen_height')
        screen_size = (self.screen_width, self.screen_height)

        display.set_caption("Galactic Salvage")

        if self.use_fullscreen:
            info = display.Info()
            screen_size = (info.current_w, info.current_h)
        self.screen = display.set_mode(screen_size)

    @staticmethod
    def toggle_fullscreen():
        display.toggle_fullscreen()
