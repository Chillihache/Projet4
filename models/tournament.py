import os.path
import json
from models.data import Data

class Tournament:

    current_round = 1
    list_of_rounds = []

    def __init__(self, name, location, start_date, end_date, list_of_players, description, number_of_rounds=4):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds

        for round in range(number_of_rounds):
            self.list_of_rounds.append(f"Round {round + 1}")

        self.list_of_players = list_of_players
        self.description = description

    def consult_tournament_information(self):

        return {"name": self.name, "location": self.location, "start_date": self.start_date, "end_date": self.end_date,
                "number_of_rounds": self.number_of_rounds, "current_round": self.current_round,
                "rounds_list": self.list_of_rounds, "list_of_players": self.list_of_players,
                "description": self.description}

    def add_tournament_in_data(self):
        list_players_names = []
        for player in self.list_of_players:
            player_name = [player.first_name + " " + player.last_name]
            list_players_names.append(player_name)

        data_tournament = {
            "Name": self.name,
            "Location": self.location,
            "Start date": self.start_date,
            "End date": self.end_date,
            "Number of rounds": self.number_of_rounds,
            "Current round": self.current_round,
            "List of rounds": self.list_of_rounds,
            "List of players": list_players_names,
            "Description": self.description
        }

        "../data/data_tournaments"

        data = Data("../data/data_tournaments")
        data.add_in_data(data_tournament)



