from random import shuffle
from helpers.json_helper import JsonHelper
from datetime import datetime



class Round:

    def __init__(self, tournament, name="", start_date="", end_date=""):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.tournament = tournament
        self.players = []
        self.matchs = []
        self.json_helper = JsonHelper("data\data_tournaments.json")

    def generate(self):
        self.name = f"Round {self.tournament.current_round}"
        self.start_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        if self.tournament.current_round == 1:
            for player in self.tournament.players:
                self.players.append([player.first_name + " " + player.last_name, 0])
            shuffle(self.players)
            for i in range(int(len(self.players)/2)):
                self.matchs.append((self.players[i], self.players[len(self.players) - i - 1]))

        else:
            previous_matchs = self.previous_matchs()
            for match in self.tournament.rounds[int(self.tournament.current_round - 2)].matchs:
                self.players.append([match[0][0], match[0][1]])
                self.players.append([match[1][0], match[1][1]])
            self.players.sort(key=lambda x: x[1], reverse=True)
            for _ in range(int(len(self.tournament.players) / 2)):
                self.find_a_match(previous_matchs)


    def find_a_match(self, previous_matchs):

        for i in range(len(self.players) - 1):
            if [self.players[0][0], self.players[i+1][0]] not in previous_matchs:
                self.matchs.append((self.players[0], self.players[i+1]))
                del self.players[0]
                del self.players[i]
                return
        self.matchs.append((self.players[0], self.players[1]))
        del self.players[0]
        del self.players[0]

    def previous_matchs(self):

        previous_matchs = []
        for round in self.tournament.rounds:
            for match in round.matchs:
                previous_matchs.append([match[0][0], match[1][0]])
                previous_matchs.append([match[1][0], match[0][0]])
        return previous_matchs

    def give_winners_points(self, choice_winners):

        for i in range(len(choice_winners)):
            match choice_winners[i]:
                case 1:
                    self.tournament.rounds[self.tournament.current_round - 1].matchs[i][0][1] += 1
                case 2:
                    self.tournament.rounds[self.tournament.current_round - 1].matchs[i][1][1] += 1
                case 3:
                    self.tournament.rounds[self.tournament.current_round - 1].matchs[i][0][1] += 0.5
                    self.tournament.rounds[self.tournament.current_round - 1].matchs[i][1][1] += 0.5
        self.tournament.rounds[self.tournament.current_round - 1].end_date = datetime.now().strftime("%Y-%m-%d %H:%M")


