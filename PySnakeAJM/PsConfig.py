from BetterConfigAJM import BetterConfigAJM as BetterConfig
from pathlib import Path
from utils import ColorConverter


class PsConfig(BetterConfig):
    """
    Class PsConfig

    This class is a subclass of BetterConfig. It represents a game configuration object that is used to store and retrieve configuration settings for the game.

    Constructor:
        def __init__(self, config_filename, config_dir, config_list_dict=None, *args, **kwargs):
            Constructs a PsConfig object with the specified configuration file name, directory, and optional configuration list dictionary. If a configuration list dictionary is not provided, the default configuration list will be used.

    Attributes:
        config_list_dict (list): A list of dictionaries representing configuration settings for different aspects of the game.

    Methods: None

    Example usage:
        # Create a PsConfig object with default configuration
        config = PsConfig("config.ini", "/path/to/config")

        # Retrieve a configuration setting
        safe_mode = config.config_list_dict[0]['DEFAULT']['safe_mode']

    Note: The PsConfig class inherits all attributes and methods from the BetterConfig class.
    """

    DATABASE_FILE_DEFAULT_PATH = Path('../Misc_Project_Files/PS_Leaderboard.db')

    def __init__(self, config_filename, config_dir, config_list_dict=None, *args, **kwargs):
        super().__init__(config_filename, config_dir, config_list_dict, *args, **kwargs)

        self.default_config = [
            {
                'DEFAULT':
                    {
                        'safe_mode': 'False',
                        'windowed_mode': 'True',
                        'screen_width': 800,
                        'screen_height': 600,
                        'sfx_volume': 100,
                        'music_volume': 100,
                        'sound_muted': 'False',
                        'bg_color': ColorConverter.rgb_to_hex((0, 0, 0)),
                        'show_fps': 'False'
                    },
                'SCOREBOARD':
                    {
                        'font_name': '',
                        'font_size': 30,
                        'scoreboard_font_color': ColorConverter.rgb_to_hex((255, 255, 255)),
                        'fps_counter_color': ColorConverter.rgb_to_hex((149, 151, 154))
                    },
                'LEADERBOARD':
                    {
                        'database_file_path': self.DATABASE_FILE_DEFAULT_PATH
                    }
            }
        ]

        if config_list_dict:
            self.config_list_dict = config_list_dict
        else:
            self.config_list_dict = self.default_config
