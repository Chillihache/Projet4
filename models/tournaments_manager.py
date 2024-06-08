from models.tournament import Tournament
from models.players_manager import PlayersManager
from helpers.json_helper import JsonHelper
from models.round import Round


class TournamentsManager:
    def __init__(self):
        self.json_helper = JsonHelper("data/data_tournaments.json")
        self.players_manager = PlayersManager()

    def create_new_tournament(self, tournament_information, players):
        tournament = Tournament(tournament_information["name"], tournament_information["location"],
                                tournament_information["start_date"], tournament_information["end_date"],
                                players, tournament_information["description"],
                                number_of_rounds=["number_of_rounds"])
        self.add_tournament_in_data(tournament)

    def add_tournament_in_data(self, tournament):
        players = []
        rounds = []
        for player in tournament.players:
            players.append({"Last name": player.last_name, "First name": player.first_name})
        for round in tournament.rounds:
            rounds.append(round.matchs)

        data_tournament = {
            "Name": tournament.name,
            "Location": tournament.location,
            "Start date": tournament.start_date,
            "End date": tournament.end_date,
            "Number of rounds": tournament.number_of_rounds,
            "Current round": tournament.current_round,
            "Rounds": rounds,
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
                rounds = []
                for player in tournament["Players"]:
                    players.append([player["Last name"], player["First name"]])
                for round in tournament["Rounds"]:
                    round_to_add = Round(tournament["Current round"], players)
                    round_to_add.matchs = round
                    rounds.append(round_to_add)

                players_found = self.players_manager.find_players(players)
                tournaments.append(Tournament(tournament["Name"], tournament["Location"],
                                              tournament["Start date"], tournament["End date"], players_found,
                                              tournament["Description"], rounds=rounds,
                                              current_round=tournament["Current round"]))
            return tournaments
        else:
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

    # TODO: A déplacer dans le tournoi
    def generate_round(self, tournament):
        # Suppress tournament from csv -> update internal list of tournaments -> Recreate the same tournament in data
        self.json_helper.delete_tournament(tournament)
        round = Round(tournament.current_round, tournament.players)
        round.generate(tournament)
        tournament.rounds.append(round)
        self.add_tournament_in_data(tournament)
        return round

    def give_winners_points(self, tournament, choice_winners):
        for i in range(len(choice_winners)):
            match choice_winners[i]:
                case 1:
                    tournament.rounds[tournament.current_round-1].matchs[i][0][1] += 1
                case 2:
                    tournament.rounds[tournament.current_round-1].matchs[i][1][1] += 1
                case 3:
                    tournament.rounds[tournament.current_round - 1].matchs[i][0][1] += 0.5
                    tournament.rounds[tournament.current_round - 1].matchs[i][1][1] += 0.5

    def close_round(self, tournament):
        self.json_helper.delete_tournament(tournament)
        tournament.current_round += 1
        self.add_tournament_in_data(tournament)




















