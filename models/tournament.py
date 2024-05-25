import os.path
import json
from tools.data import Data

class Tournament:

    def __init__(self, name, location, start_date, end_date, players, description, number_of_rounds=4):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        
        self.number_of_rounds = number_of_rounds
        
        self.current_round = 1
        self.rounds = []

        for round in range(number_of_rounds):
            self.rounds.append(f"Round {round + 1}")

        self.players = players
        self.description = description

    def consult_tournament_information(self):

        return {"name": self.name, "location": self.location, "start_date": self.start_date, "end_date": self.end_date,
                "number_of_rounds": self.number_of_rounds, "current_round": self.current_round,
                "rounds": self.rounds, "players": self.players,
                "description": self.description}
