from enum import IntEnum
from views.main_menu_view import MainMenuView
from models.players_manager import PlayersManager

class MainMenu:
    class Options(IntEnum):
        DEFAULT = 0
        ADD_PLAYER = 1
        TOURNAMENTS = 2
        REPORTS = 3
        EXIT = 4

    def __init__(self):
        self.player_manager = PlayersManager()

    def main_loop(self):
        value = MainMenu.Options.DEFAULT
        while value != MainMenu.Options.EXIT:
            value = MainMenu.Options(int(MainMenuView.input_selection(MainMenu.Options)))