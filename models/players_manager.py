from views.view import View
from models.player import Player
from tools.data import Data


class PlayersManager:
    def __init__(self):
        self.load_players()

    def load_players(self):
        self.players = [] # Implementer le chargement des joueurs depuis le json

    def add_new_player(self):
        new_player_information = View.ask_new_player_information()
        new_player = Player(last_name=new_player_information[0], first_name=new_player_information[1],
                            date_of_birth=new_player_information[2])
        self.add_player_in_data(new_player)
        View.player_created()


    def add_player_in_data(self):
        data_player = {
            "Last name": self.last_name,
            "First name": self.first_name,
            "Date of birth": self.date_of_birth
        }

        data = Data("../data/data_players")
        data.add_in_data(data_player)

    def find_a_player(self, player_to_find):
        for player in self.players:
            if (player["Last name"].lower() == player_to_find[0].lower() and
                    player["First name"].lower() == player_to_find[1].lower()):
                return player
        return None

    @staticmethod
    def consult_data_players():
        data = Data("../data/data_players")
        data_players = data.get_data()
        data_players.sort(key=lambda players: players["Last name"].lower())
        if data_players:
            View.show_data_players(data_players)
        else:
            View.empty_data_players()




