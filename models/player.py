import json
import os.path
from models.data import Data


class Player:

    def __init__(self, last_name, first_name, date_of_birth):

        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth

    def add_player_in_data(self):
        data_player = {
            "Last name": self.last_name,
            "First name": self.first_name,
            "Date of birth": self.date_of_birth
        }

        data = Data("../data/data_players")
        data.add_in_data(data_player)

    @staticmethod
    def find_a_player(player_to_find, data_players):
        for player in data_players:
            if (player["Last name"].lower() == player_to_find[0].lower() and
                    player["First name"].lower() == player_to_find[1].lower()):
                return player
        return None
