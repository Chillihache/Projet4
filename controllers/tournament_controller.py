from models.tournaments_manager import TournamentManager
from views.create_tournament_view import CreateTournamentView
from models.players_manager import PlayersManager

class TournamentController:

    def __init__(self):

        self.tournaments_manager = TournamentManager()
        self.create_tournament_view = CreateTournamentView()
        self.player_manager = PlayersManager()

    def create_new_tournament(self):
        self.create_tournament_view.warning_message()
        tournament_information = self.create_tournament_view.ask_new_tournament_information()
        players_to_find = self.create_tournament_view.ask_players_to_add(tournament_information)
        players_found = self.player_manager.find_players(players_to_find)
        if players_found:
            self.tournaments_manager.create_new_tournament(tournament_information, players_found)
        else:
            CreateTournamentView.error_message()



        tournament = Tournament(tournament_information["name"], tournament_information["location"],
                                tournament_information["start_date"], tournament_information["end_date"],
                                players, tournament_information["description"])
        tournament.add_tournament_in_data()
        View.tournament_created()