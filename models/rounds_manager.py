from models.round import Round

class RoundsManager:

    def __init__(self):
        pass

    def change_round(self, tournament):
        tournament.current_round += 1
        print(tournament.current_round)