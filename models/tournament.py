

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

    def consult_tournament_information(self):

        return {"Name": self.name, "Location": self.location, "Start_date": self.start_date, "End_date": self.end_date,
                "Number_of_rounds": self.number_of_rounds, "Current_round": self.current_round,
                "Rounds": self.rounds, "Players": self.players,
                "Description": self.description}
