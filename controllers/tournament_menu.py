from enum import IntEnum
from views.tournament_menu_view import TournamentMenuView
from controllers.tournament_controller import TournamentController

class TournamentMenu:
    class Options(IntEnum):
        DEFAULT = 0
        CREATE = 1
        MANAGE = 2
        EXIT = 3

    def __init__(self):
        self.tournament_controller = TournamentController()

    def loop(self):
        value = TournamentMenu.Options.DEFAULT
        while value != TournamentMenu.Options.EXIT:
            match value:
                case TournamentMenu.Options.CREATE:
                    self.tournament_controller.create_new_tournament()
                case TournamentMenu.Options.MANAGE:
                    pass
            value = TournamentMenu.Options(int(TournamentMenuView.input_selection(TournamentMenu.Options)))