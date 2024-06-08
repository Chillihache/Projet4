import random
from helpers.json_helper import JsonHelper


class Round:

    def __init__(self, current, players):

        self.current = current
        self.players = players
        self.matchs = []
        self.json_helper = JsonHelper("data\data_tournaments.json")
        self.players_and_scores = []

    def generate(self, tournament):
        if self.current == 1:
            for player in self.players:
                self.players_and_scores.append([player.first_name + " " + player.last_name, 0])
            random.shuffle(self.players_and_scores)
            for i in range(int(len(self.players_and_scores)/2)):
                self.matchs.append((self.players_and_scores[i],
                                    self.players_and_scores[len(self.players_and_scores)-i-1]))

        else:
            for match in tournament.rounds[self.current - 2].matchs:
                self.players_and_scores.append(match[0])
                self.players_and_scores.append(match[1])

            self.players_and_scores = sorted(self.players_and_scores, key=lambda x: x[1], reverse=True)

            previous_matchs = []
            for i in range(self.current - 1):
                for match in (tournament.rounds[i].matchs):
                    previous_matchs.append([match[0][0], match[1][0]])
                    previous_matchs.append([match[1][0], match[0][0]])

            while len(self.players_and_scores) != 0:
                self.find_a_match(previous_matchs)
    def find_a_match(self, previous_matchs):

        for j in range(len(self.players_and_scores)):
            if [self.players_and_scores[0][0], self.players_and_scores[j][0]] not in previous_matchs:
                self.matchs.append((self.players_and_scores[0], self.players_and_scores[j]))
                del self.players_and_scores[0]
                del self.players_and_scores[j]
                break


































