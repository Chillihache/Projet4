from models.tournaments_manager import TournamentsManager
from views.create_tournament_view import CreateTournamentView
from models.players_manager import PlayersManager
from views.report_tournaments_view import ReportTournamentsView
from views.manage_tournament_view import ManageTournamentView
from helpers.json_helper import JsonHelper
from models.round import Round


class TournamentsController:

    def __init__(self):

        self.tournaments_manager = TournamentsManager()
        self.create_tournament_view = CreateTournamentView()
        self.player_manager = PlayersManager()
        self.report_tournaments_view = ReportTournamentsView()
        self.manage_tournament_view = ManageTournamentView()


    def create_new_tournament(self):
        self.create_tournament_view.warning_message()
        tournament_information = self.create_tournament_view.ask_new_tournament_information()
        players_to_find = self.create_tournament_view.ask_players_to_add(tournament_information)
        players_found = self.player_manager.find_players(players_to_find)
        if players_found:
            self.tournaments_manager.create_new_tournament(tournament_information, players_found)
            self.create_tournament_view.tournament_created()
        else:
            CreateTournamentView.error_message()

    def load_tournaments(self):
        tournaments = self.tournaments_manager.load_tournaments()
        return tournaments

    def choose_a_tournament(self):
        tournament_to_find = self.report_tournaments_view.ask_tournament_name()
        tournament_found = self.tournaments_manager.find_a_tournament(tournament_to_find)
        return tournament_found

    def report_tournaments(self):
        tournaments = self.load_tournaments()
        self.report_tournaments_view.show_tournaments_list(tournaments)

    def report_tournament_name_and_dates(self):
        tournament = self.choose_a_tournament()
        self.report_tournaments_view.show_tournament_name_dates(tournament)

    def report_tournament_players(self):
        tournament = self.choose_a_tournament()
        self.report_tournaments_view.show_tournament_players(tournament)

    def manage_tournament(self):
        tournament = self.choose_a_tournament()
        if tournament:
            if len(tournament.rounds) == tournament.current_round - 1:
                self.generate_new_round(tournament)
            else:
                self.get_winners(tournament)
                self.tournaments_manager.close_round(tournament)

        else:
            self.manage_tournament_view.tournament_not_found()

    def generate_new_round(self, tournament):

            self.manage_tournament_view.generate_round(tournament.current_round)
            round = self.tournaments_manager.generate_round(tournament)
            self.manage_tournament_view.round_generated(tournament, round)

    def get_winners(self, tournament):
        choice_winners = []
        for match in tournament.rounds[tournament.current_round-1].matchs:
            choice = self.manage_tournament_view.ask_winner(match)
            choice_winners.append(choice)
        self.tournaments_manager.give_winners_points(tournament, choice_winners)
        self.manage_tournament_view.show_winners(tournament)






















