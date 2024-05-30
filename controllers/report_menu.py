from views.report_menu_view import ReportMenuView
from enum import IntEnum
from controllers.player_controller import PlayerController



class ReportMenu:
    class Options(IntEnum):
        DEFAULT = 0
        PLAYERS = 1
        TOURNAMENTS = 2
        TOURNAMENT_NAME_DATES = 3
        TOURNAMENT_PLAYERS = 4
        TOURNAMENT_ROUNDS_MATCHS = 5
        EXIT = 6

    def __init__(self):
        self.report_menu_view = ReportMenuView()
        self.player_controller = PlayerController()


    def loop(self):
        value = ReportMenu.Options.DEFAULT
        while value != ReportMenu.Options.EXIT:
            match value:
                case ReportMenu.Options.PLAYERS:
                    self.player_controller.report_players()
                case ReportMenu.Options.TOURNAMENTS:
                    pass
                case ReportMenu.Options.TOURNAMENT_NAME_DATES:
                    pass
                case ReportMenu.Options.TOURNAMENT_PLAYERS:
                    pass
                case ReportMenu.Options.TOURNAMENT_ROUNDS_MATCHS:
                    pass

            value = ReportMenu.Options(int(ReportMenuView.input_selection(ReportMenu.Options)))
