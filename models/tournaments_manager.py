from models.tournament import Tournament
from models.players_manager import PlayersManager
from helpers.json_helper import JsonHelper


class TournamentsManager:
    def __init__(self):
        self.json_helper = JsonHelper("data/data_tournaments.json")
        self.players_manager = PlayersManager()

    def create_new_tournament(self, tournament_information, players):
        tournament = Tournament(tournament_information["name"], tournament_information["location"],
                                tournament_information["start_date"], tournament_information["end_date"],
                                players, tournament_information["description"])
        self.add_tournament_in_data(tournament)

    def add_tournament_in_data(self, tournament):
        players = []
        for player in tournament.players:
            players.append(player.first_name + " " + player.last_name)

        data_tournament = {
            "Name": tournament.name,
            "Location": tournament.location,
            "Start date": tournament.start_date,
            "End date": tournament.end_date,
            "Number of rounds": tournament.number_of_rounds,
            "Current round": tournament.current_round,
            "Rounds": tournament.rounds,
            "Players": players,
            "Description": tournament.description
        }
        self.json_helper.add_in_data(data_tournament)

    def load_tournaments(self):

        data_tournaments = self.get_data_tournaments()
        tournaments = []
        if data_tournaments:
            for tournament in data_tournaments:
                players = []
                for player in tournament["Players"]:
                    players.append([player[player.find(" ")+1:], player[:player.find(" ")]])
                players_found = self.players_manager.find_players(players)
                tournaments.append(Tournament(tournament["Name"], tournament["Location"],
                                              tournament["Start date"], tournament["End date"], players_found,
                                              tournament["Description"]))
            return tournaments
        else :
            return None

    def get_data_tournaments(self):
        data_tournaments = self.json_helper.get_data()
        return data_tournaments

    def find_a_tournament(self, tournament_to_find):
        tournaments = self.load_tournaments()
        for tournament in tournaments:
            if tournament.name.lower() == tournament_to_find.lower():
                return tournament
        return None












