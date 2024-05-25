from views.view import View
from models.player import Player
from models.tournament import Tournament
from helpers.json_helper import JsonHelper

class TournamentManager:
    def __init__(self) -> None:
        self.tournaments = []

    def create_new_tournament(self):
        View.warning_message()
        tournament_information = View.ask_new_tournament_information()
        players = []
        for _ in range(tournament_information["number_of_players"]):
            player_to_add = TournamentManager.add_player_in_tournament()
            if player_to_add:
                player_add = Player(player_to_add["Last name"], player_to_add["First name"],
                                    player_to_add["Date of birth"])
                players.append(player_add)
            else:
                return
        tournament = Tournament(tournament_information["name"], tournament_information["location"],
                                tournament_information["start_date"], tournament_information["end_date"],
                                players, tournament_information["description"])
        tournament.add_tournament_in_data()
        View.tournament_created()

    def add_tournament_in_data(self):
        players_names = []
        for player in self.players:
            player_name = [player.first_name + " " + player.last_name]
            players_names.append(player_name)

        data_tournament = {
            "Name": self.name,
            "Location": self.location,
            "Start date": self.start_date,
            "End date": self.end_date,
            "Number of rounds": self.number_of_rounds,
            "Current round": self.current_round,
            "Rounds": self.rounds,
            "Players": players_names,
            "Description": self.description
        }

        "../data/data_tournaments"

        data = Data("../data/data_tournaments")
        data.add_in_data(data_tournament)

    @staticmethod
    def add_player_in_tournament():

        player_to_find = View.find_a_player()
        data = Data("../data/data_players")
        data_players = data.get_data()
        player_found = Player.find_a_player(player_to_find, data_players)
        if player_found:
            View.player_found(player_found)
            return player_found
        else:
            View.player_not_found(player_to_find)
            return None

    @staticmethod
    def consult_data_tournaments():
        data = Data("../data/data_tournaments")
        data_tournament = data.get_data()
        View.show_tournaments_names_and_start_date(data_tournament)


    @staticmethod
    def consult_tournament_information():
        tournament_to_find = View.ask_tournament_to_find()
        data = Data("../data/data_tournaments")
        data_tournament = data.get_data()
        for tournament in data_tournament:
            if tournament["Name"] == tournament_to_find:
                View.show_tournament_information(tournament)
            else:
                View.tournament_not_found()





