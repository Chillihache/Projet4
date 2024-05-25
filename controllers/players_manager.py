from views.view import View
from models.player import Player
from models.data import Data


class PlayersManager:

    @staticmethod
    def add_new_player():
        new_player_information = View.ask_new_player_information()
        new_player = Player(last_name=new_player_information[0], first_name=new_player_information[1],
                            date_of_birth=new_player_information[2])
        new_player.add_player_in_data()
        View.player_created()

    @staticmethod
    def consult_data_players():
        data = Data("../data/data_players")
        data_players = data.get_data()
        data_players.sort(key=lambda players: players["Last name"].lower())
        if data_players:
            View.show_data_players(data_players)
        else:
            View.empty_data_players()




