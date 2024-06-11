from helpers.json_helper import JsonHelper
from models.round import Round

class Tournament:

    def __init__(self, name, location, start_date, end_date, players, description, number_of_rounds=4, current_round=1, rounds=None):

        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        
        self.number_of_rounds = number_of_rounds
        
        self.current_round = current_round
        self.rounds = []
        try:
            for round in rounds:
                self.rounds.append(round)
        except:
            TypeError



        self.players = players
        self.description = description
        self.json_helper = JsonHelper("data\data_tournaments.json")
        self.round = Round(self)

    def generate_round(self):

        from models.tournaments_manager import TournamentsManager
        tournament_manager = TournamentsManager()

        self.json_helper.delete_tournament(self)
        self.round.generate()
        self.rounds.append(self.round)
        tournament_manager.add_tournament_in_data(self)
        return round

    def close_round(self):

        from models.tournaments_manager import TournamentsManager
        tournament_manager = TournamentsManager()
        self.json_helper.delete_tournament(self)
        self.current_round += 1
        tournament_manager.add_tournament_in_data(self)
